import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBDYRC0nLhQOKmYXrzJa-QgW-LYEgZjCyw")

from load import rag_chatbot_gemini
from load import collection

st.title("Healthcare RAG Chatbot")
st.write("Ask Questions about India's Primary Health Care")

user_question=st.text_input("Enter your Question: ")

if st.button("Get Answer"):
    if user_question.strip()!="":
        with st.spinner("Generating answer"):
            answer=rag_chatbot_gemini(user_question)
        st.success("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a valid question")
        