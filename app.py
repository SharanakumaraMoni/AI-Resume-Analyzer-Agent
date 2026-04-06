import streamlit as st
from rag.loader import load_data
from rag.splitter import split_docs
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from llm.groq_llm import load_llm
from chains.rag_chain import create_chain
from dotenv import load_dotenv
load_dotenv()

st.title("RAG Chatbot 🤖")

file = st.file_uploader("Upload PDF", type="pdf")

if file:
    docs = load_data(file)
    texts = split_docs(docs)
    embeddings = get_embeddings()
    db = create_vectorstore(texts, embeddings)
    retriever = get_retriever(db)
    llm = load_llm()
    chain = create_chain(llm, retriever)

    question = st.text_input("Ask a question about the PDF:")

    if question:
        with st.spinner("Generating answer..."):
            answer = chain.invoke(question)
        st.write("Answer:", answer)