def get_retriever(db):
    retriever = db.as_retriever()
    return retriever