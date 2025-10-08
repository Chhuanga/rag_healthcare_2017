# Healthcare RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that provides information about India's Primary Health Care system using 2017 healthcare data. The chatbot uses ChromaDB for vector storage, Sentence Transformers for embeddings, and Google's Gemini AI for generating responses.

## Features

- Query healthcare data across multiple categories (hospitals, clinics, staff, facilities)
- Semantic search through healthcare documents using vector embeddings
- AI-powered responses using Google's Gemini model
- Interactive web interface built with Streamlit
- Supports multiple CSV data sources

## Technology Stack

- **Frontend**: Streamlit
- **Vector Database**: ChromaDB
- **Embeddings**: SentenceTransformer (all-MiniLM-L6-v2)
- **LLM**: Google Gemini 2.5 Flash
- **Data Processing**: Pandas
- **Language**: Python

## Project Structure

```
rag_bot/
├── frontend.py          # Streamlit web interface
├── load.py             # Data loading and RAG functions
├── data/               # CSV data files (not tracked in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Data Source

This project uses the "India Primary Health Care Data (2017)" from Kaggle:
https://www.kaggle.com/datasets/webaccess/india-primary-health-care-data

To download:
1. Go to the Kaggle link above.
2. Download the CSV files.
3. Place them in the `data/` folder of this repository.

### Expected Data Files

The system expects CSV files in the `data/` folder with healthcare information including:
- Primary Health Care Centers (PHCS)
- Community Health Centers (CHCS)
- Sub-centers and staff data
- Facility information
- Medical personnel data

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chhuanga/rag_healthcare_2017.git
   cd rag_healthcare_2017
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas sentence-transformers chromadb google-generativeai
   ```

4. **Set up data**
   - Download the Kaggle dataset (see Data Source section above)
   - Create a `data/` folder in the project root
   - Place all CSV files in the `data/` folder

5. **Configure API Key**
   - Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the API key in both `frontend.py` and `load.py`
   - **Security Note**: For production, use environment variables instead of hardcoding API keys

## Usage

1. **Prepare the data and embeddings** (run once)
   ```bash
   python load.py
   ```

2. **Start the Streamlit app**
   ```bash
   streamlit run frontend.py
   ```

3. **Access the web interface**
   - Open your browser to `http://localhost:8501`
   - Enter healthcare-related questions
   - Get AI-powered responses based on the 2017 healthcare data

## Example Queries

- "How many Primary Health Centers are there in Meghalaya?"
- "List the healthcare facilities in West Bengal"
- "What is the doctor-to-population ratio in rural areas?"
- "Show me information about medical staff in community health centers"

## How It Works

1. **Data Loading**: CSV files are loaded and processed into text documents
2. **Embedding Creation**: Each document is converted to vector embeddings using SentenceTransformer
3. **Vector Storage**: Embeddings are stored in ChromaDB for fast similarity search
4. **Query Processing**: User queries are embedded and matched against stored documents
5. **Response Generation**: Retrieved context is sent to Gemini AI to generate natural language responses

## Configuration

- **Collection Name**: `healthcare_documentations4` (ChromaDB)
- **Embedding Model**: `all-MiniLM-L6-v2`
- **LLM Model**: `gemini-2.5-flash`
- **Default Results**: Top 3 most relevant documents per query

## Security Notes

- ⚠️ **API Keys**: The current code contains hardcoded API keys. For production use:
  ```python
  import os
  api_key = os.getenv('GEMINI_API_KEY')
  ```
- 🔒 **Data Privacy**: Healthcare data is kept local and not uploaded to git
- 🛡️ **Environment**: Use `.env` files for sensitive configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please ensure compliance with data usage terms from Kaggle and respect healthcare data privacy regulations.

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure `load.py` exists and contains the required functions
2. **Data Not Found**: Ensure CSV files are in the `data/` folder
3. **API Key Error**: Verify your Gemini API key is valid and has sufficient quota
4. **ChromaDB Issues**: Delete any existing ChromaDB files and recreate the collection

### Support

If you encounter issues:
1. Check that all dependencies are installed
2. Verify the data files are in the correct location
3. Ensure your API key is valid
4. Check the console for detailed error messages

---

**Built with ❤️ for healthcare data analysis and AI-powered information retrieval**
