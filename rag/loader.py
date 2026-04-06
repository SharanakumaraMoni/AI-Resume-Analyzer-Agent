from PyPDF2 import PdfReader
from langchain.schema import Document

def load_data(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    docs = [Document(page_content=text)]
    return docs