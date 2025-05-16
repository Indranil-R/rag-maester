
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Method to clean the text
# This function removes common watermark or repeated footer content
def clean_text(text):
    """
    Removes common watermark or repeated footer content.
    """
    removal_phrases = [
        "(c) Amity University Online",
        "Notes",
        "Amity Directorate of Distance & Online Education",
        "Introduction to E-Governance"
    ]
    for phrase in removal_phrases:
        text = text.replace(phrase, "")
    return text.strip()

def load_and_split_pdf(doc_path):
    """
    Loads a PDF from the 6th page onward, cleans watermark text, and splits efficiently.

    Args:
        doc_path (str): Full path to the PDF file.

    Returns:
        list: A list of cleaned and chunked documents.
    """
    # Load all pages
    loader = PyPDFLoader(file_path=doc_path, mode="page")
    all_pages = loader.load()

    # Ignore the first 5 pages
    relevant_pages = all_pages[5:]

    # Clean watermark from each page
    for page in relevant_pages:
        page.page_content = clean_text(page.page_content)

    # Use a more efficient splitter config
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=250,
        separators=["\n\n", "\n", ".", " "],  # smart fallback separator list
    )

    # Split and return
    return text_splitter.split_documents(relevant_pages)

def process_documents(documents_path_list: list[str]) -> list:
    """
    Processes a list of PDF document paths.
    For each document, it loads content from the 6th page onward,
    cleans it, and splits it into chunks using the `load_and_split_pdf` function.

    Args:
        documents_path_list (list[str]): A list of full file paths to PDF documents.

    Returns:
        list: A single list containing all cleaned and chunked Document objects
              from all successfully processed PDF files.
    """
    all_processed_chunks = []  # Initialize an empty list to store chunks from all documents

    # Iterate over each document path in the provided list
    for doc_path in documents_path_list:
        print(f"Processing document: {doc_path}")
        try:
            # Call the existing function to process a single document
            single_doc_chunks = load_and_split_pdf(doc_path)

            # Add the chunks from the current document to the main list
            if single_doc_chunks: # Ensure there are chunks to add
                all_processed_chunks.extend(single_doc_chunks)
                print(f"Successfully processed and extracted {len(single_doc_chunks)} chunks from {doc_path}")
            else:
                print(f"No relevant chunks extracted from {doc_path} (e.g., too few pages or empty content after cleaning).")

        except FileNotFoundError:
            print(f"Error: Document not found at {doc_path}. Skipping this document.")
        except Exception as e:
            # Catch any other errors during the processing of a single document
            print(f"Error processing document {doc_path}: {e}. Skipping this document.")

    return all_processed_chunks

