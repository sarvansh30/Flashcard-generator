from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def embed_and_store(chunks):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory="./chroma_db",
        collection_name="flashcards"
    )
    vectordb.persist()
    return vectordb
