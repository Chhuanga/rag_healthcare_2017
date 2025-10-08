import os
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with environment variable
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

genai.configure(api_key=api_key)

# Load data and create collection
def load_data_and_create_collection():
    folder_path = "data"
    dataframes = {}
    
    # Load CSV files
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            dataframes[file_name] = df
            print(f"Loaded {file_name} with {len(df)} rows.")
    
    # Create ChromaDB collection
    client = chromadb.Client()
    try:
        collection = client.create_collection(name="healthcare_documentations4")
    except:
        collection = client.get_collection("healthcare_documentations4")
    
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Only add documents if collection is empty
    if collection.count() == 0:
        docs = []
        ids = []
        
        for file_name, df in dataframes.items():
            for i, row in df.iterrows():
                text = f"File: {file_name}\n" + "\n".join([f"{col}: {row[col]}" for col in df.columns])
                docs.append(text)
                ids.append(f"{file_name}_{i}")
        
        embeddings = embedder.encode(docs).tolist()
        collection.add(documents=docs, embeddings=embeddings, ids=ids)
    
    return collection, embedder

# Initialize collection and embedder
collection, embedder = load_data_and_create_collection()

def rag_chatbot_gemini(query, top_k=3):
    # Retrieve context from Chroma
    results = collection.query(query_texts=[query], n_results=top_k)
    docs = results["documents"][0]
    
    # Combine the top results into a single context window
    context = "\n\n".join(docs)
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""You are a healthcare Assistant AI.
    Use the following information to answer the question accurately.
    If the answer is not found, say "I don't have enough data for that."
    
    Context: {context}
    Question: {query}
    Answer: 
    """
    response = model.generate_content(prompt)
    return response.text.strip()