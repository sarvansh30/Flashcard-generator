from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os

def load_and_chunk_pdf(uploaded_file):
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)
