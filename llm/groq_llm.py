from langchain_groq import ChatGroq
import os

def load_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",   # ✅ updated
        groq_api_key=os.getenv("GROQ_API_KEY")
    )