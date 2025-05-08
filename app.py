import streamlit as st
from main import process_pdf_and_generate_flashcards

# Custom CSS for flashcard styling
FLASHCARD_CSS = """
<style>
.card {
    padding: 15px;
    margin: 10px 0;
    background-color: #f9f9f9;
    border-left: 4px solid #4CAF50;
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
}
.card q {
    font-style: italic;
}
.card a {
    margin-top: 5px;
    display: block;
}
</style>
"""

st.set_page_config(page_title="Flashcard Generator", layout="wide")
st.markdown(FLASHCARD_CSS, unsafe_allow_html=True)
st.title("🧠 PDF Flashcard Generator")

# File upload and topic input
uploaded_file = st.file_uploader("Upload your study PDF", type=["pdf"])
topic = st.text_input("Enter a topic for flashcards")

if st.button("Generate Flashcards"):
    if not uploaded_file or not topic:
        st.warning("Please upload a PDF and enter a topic.")
    else:
        with st.spinner("Processing PDF and generating flashcards..."):
            raw_output, context = process_pdf_and_generate_flashcards(uploaded_file, topic)
        # Post-process raw output into list of (Q,A) pairs
        cards = []
        for block in raw_output.strip().split("Flashcard ")[1:]:
            lines = block.splitlines()
            if len(lines) >= 3 and lines[1].startswith("Q") and lines[2].startswith("A"):
                q = lines[1].split(':', 1)[1].strip()
                a = lines[2].split(':', 1)[1].strip()
                cards.append((q, a))

        # Display flashcards as styled cards
        st.subheader("📋 Generated Flashcards")
        for i, (q, a) in enumerate(cards, 1):
            st.markdown(f"<div class='card'><q>{q}</q><a><strong>A:</strong> {a}</a></div>", unsafe_allow_html=True)

        # Optionally show retrieved context
        with st.expander("Show Retrieved Context"):
            st.write(context)