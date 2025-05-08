from utils.pdf_loader import load_and_chunk_pdf
from utils.embeddings import embed_and_store
from utils.retriever import retrieve_relevant_chunks
from utils.llm_interface import generate_flashcards


def process_pdf_and_generate_flashcards(uploaded_file, topic):
    chunks = load_and_chunk_pdf(uploaded_file)
    vectordb = embed_and_store(chunks)
    context = retrieve_relevant_chunks(vectordb, topic)
    flashcards = generate_flashcards(context, topic)
    return flashcards, context