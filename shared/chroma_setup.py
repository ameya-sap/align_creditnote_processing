import os
import chromadb
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Sample Data')

def process_and_index():
    print(f"Initializing ChromaDB at {CHROMA_DB_DIR}")
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    
    # Create or get collection
    collection = client.get_or_create_collection(name="policy_documents")
    
    # Files to process
    files_to_index = [
        "File2-CuCo-2025-Master-Policy.pdf",
        "File3-EMEA-Work-Instruction-Document.pdf",
        "File4-Exception-&-Goodwill-Approval-Matrix.pdf"
    ]
    
    converter = DocumentConverter()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    
    for filename in files_to_index:
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping.")
            continue
            
        print(f"Processing {filename} with docling...")
        try:
            # Convert document to text using docling
            result = converter.convert(filepath)
            full_text = result.document.export_to_markdown()
            
            # Split text using langchain
            chunks = text_splitter.create_documents([full_text])
            
            # Add to Chroma
            for i, chunk in enumerate(chunks):
                doc_id = f"{filename}_chunk_{i}"
                collection.upsert(
                    documents=[chunk.page_content],
                    metadatas=[{"source": filename, "chunk": i}],
                    ids=[doc_id]
                )
            print(f"Indexed {len(chunks)} chunks for {filename}")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    process_and_index()
