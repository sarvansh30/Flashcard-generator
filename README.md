
# 🧠 Flashcard Generator

A Streamlit-based web app that automatically generates flashcards from PDF documents using a Retrieval-Augmented Generation (RAG) pipeline powered by open-source LLMs.

## 🚀 Features

- 📄 Upload any PDF document (e.g. lecture notes, reports, textbooks)
- 🔍 Semantic chunking and indexing using LangChain + ChromaDB
- 🧠 Retrieval-Augmented Generation (RAG) to generate flashcards on a chosen topic
- ✨ Clean, styled flashcard display using HTML/CSS inside Streamlit
- 🧱 Modular codebase with lazy loading and optimized prompt engineering

## 📁 Project Structure

```
flashcard_app/
├── app.py                  # Streamlit interface
├── main.py                 # Core application logic
├── requirements.txt        # All dependencies
├── config.py               # Optional configs
├── utils/
│   ├── pdf_loader.py       # PDF loading and chunking
│   ├── embedding.py        # Embedding and vector store logic
│   ├── retriever.py        # Vector search logic
│   └── llm_interface.py    # Flashcard generation via LLM
└── chroma_db/              # Persistent ChromaDB index
```

## 🧠 How It Works

1. **Upload a PDF**: The user uploads a document (e.g., study material).
2. **Chunk & Embed**: The app extracts text and splits it into overlapping chunks using LangChain.
3. **Vector Storage**: Chunks are embedded using a Sentence-Transformer and stored in ChromaDB.
4. **RAG Generation**: When a user asks for flashcards on a topic, the app retrieves the most relevant chunks and sends them to a Hugging Face LLM to generate concise Q&A pairs.
5. **Display**: The flashcards are displayed in a clean, scrollable format.

## 📦 Installation

```bash
git clone https://github.com/sarvansh30/Flashcard-generator
cd Flashcard_generator
streamlit run app.py
```

> ⚠️ Note: This project uses `google/flan-t5-base` via Hugging Face. Make sure you have `transformers` and `langchain-huggingface` installed.

## 🔧 Dependencies

- Python 3.8+
- Streamlit
- LangChain
- Hugging Face Transformers
- ChromaDB
- Sentence-Transformers
- PyMuPDF


## 📚 Use Cases

- Study aid for students
- Quick review from lecture PDFs
- Domain-specific flashcard generation from any document
