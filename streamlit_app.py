import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer

# --- Setup ---
st.set_page_config(page_title="RAG Maester", layout="wide")
st.title("📚 RAG Maester: Your AI Scholar")

# --- Load Gemini-Compatible Tokenizer ---
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
length_function = lambda x: len(tokenizer.encode(x))

# --- Define Utility Functions ---
def clean_text(text):
    removal_phrases = [
        "(c) Amity University Online",
        "Notes",
        "Amity Directorate of Distance & Online Education"
    ]
    for phrase in removal_phrases:
        text = text.replace(phrase, "")
    return text.strip()

def process_documents(uploaded_files):
    all_texts = []

    for uploaded_file in uploaded_files:
        doc_path = os.path.join("temp_docs", uploaded_file.name)
        with open(doc_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        loader = PyPDFLoader(file_path=doc_path, mode="page")
        all_pages = loader.load()
        relevant_pages = all_pages[5:]

        for page in relevant_pages:
            page.page_content = clean_text(page.page_content)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            separators=["\n\n", "\n", ".", " "],
            length_function=length_function,
        )

        chunks = text_splitter.split_documents(relevant_pages)
        all_texts.extend(chunks)

    return all_texts

# --- File Upload UI ---
st.sidebar.header("Upload PDFs")
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing documents..."):
        os.makedirs("temp_docs", exist_ok=True)
        texts = process_documents(uploaded_files)

    st.success(f"Processed {len(texts)} chunks from {len(uploaded_files)} documents.")

    # Display a few chunks
    st.subheader("📄 Preview of Extracted Chunks")
    for i, chunk in enumerate(texts[:5]):
        st.markdown(f"**Chunk {i+1}:**")
        st.code(chunk.page_content[:1000])
else:
    st.info("Please upload at least one PDF to get started.")
