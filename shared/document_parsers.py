import os
import re
from pypdf import PdfReader

# Build an absolute path to the project root relative to this file's location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def extract_sales_orders_from_pdf(filepath: str):
    # Resolve the provided path (e.g. "Sample Data/...") relative to the project root
    abs_path = os.path.join(PROJECT_ROOT, filepath)
    if not os.path.exists(abs_path):
        return f"Error: Could not find file at {abs_path}"
        
    reader = PdfReader(abs_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        
    return text

def parse_csv_to_dict(filepath: str):
    import pandas as pd
    abs_path = os.path.join(PROJECT_ROOT, filepath)
    if not os.path.exists(abs_path):
        return []
        
    df = pd.read_csv(abs_path)
    return df.to_dict(orient="records")
