from langchain.vectorstores import FAISS

def create_vectorstore(texts, embeddings):
    db = FAISS.from_documents(texts, embeddings)
    return db