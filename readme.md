# RAG Maester: Your AI Scholar

RAG Maester is an AI-powered tool designed to help students, researchers, and professionals analyze and interact with academic documents using **Retrieval-Augmented Generation (RAG)**. Built with **LangChain**, **Streamlit**, and **transformers**, it processes PDF documents into semantically chunked data ready for embedding and intelligent querying.

---

## Features

- Upload and process multiple PDF files
- Automatically clean watermarks and repeated footer texts
- Start reading from the 6th page (skips TOC/front matter)
- Split documents into clean, overlapping chunks
- Compatible with Gemini or other token-length-sensitive models
- Preview processed content in a modern Streamlit interface

---

## Project Structure

```
rag-maester/
├── RAG_Workflow.ipynb         # Notebook for exploration and RAG logic
├── streamlit_app.py           # Streamlit UI app for document upload and preview
├── rag_utils.py               # Shared logic for cleaning and processing documents
├── docs/                      # Folder containing input PDFs
├── temp_docs/                 # Temporary folder for uploads
└── requirements.txt           # List of dependencies
```

---

## Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/rag-maester.git
cd rag-maester
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.8+ and `streamlit`, `langchain`, `transformers`, `PyMuPDF` installed.

---

## Usage

### In Jupyter Notebook
```python
from rag_utils import process_documents
chunks = process_documents(["docs/your_file.pdf"])
print(chunks[0].page_content)
```

### Run Streamlit UI
```bash
streamlit run streamlit_app.py
```

> This will open the RAG Maester interface in your browser.

---

## Coming Soon

- Vector embedding and similarity search
- Integration with Gemini / OpenAI / Azure AI models
- Document validation workflows
- Semantic search with UI filters

---

## Acknowledgments

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)

---

## License

MIT License.

---

**RAG Maester** – Bringing intelligence to your documents.
