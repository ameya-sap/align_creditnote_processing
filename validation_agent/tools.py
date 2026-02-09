import os
import chromadb

CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')

def query_policy(query: str) -> str:
    """
    Query the CuCo-2025 and EMEA Work Instruction policies to validate credit request rules.
    Use this to check if a region is eligible or what discount applies to what reason.
    """
    if not os.path.exists(CHROMA_DB_DIR):
        return "Warning: Policy database not initialized. Please run python shared/chroma_setup.py"
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    collection = client.get_or_create_collection(name="policy_documents")
    results = collection.query(query_texts=[query], n_results=3)
    
    if results and results['documents']:
        return "\n\n".join(results['documents'][0])
    return "No relevant policy found."

def map_reason_to_category(reason: str) -> str:
    """
    Maps a user-provided reason (e.g. "PSA") to an official category 
    based on the workflow matrix.
    """
    reason_lower = reason.lower()
    if "psa" in reason_lower or "product deficiency" in reason_lower:
        return "Clinical & Product Deficiency"
    if "invisalign first" in reason_lower:
        return "FIRST-COMP"
    return "Unknown Category"
