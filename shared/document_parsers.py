import os
import re
from pypdf import PdfReader

# This simple parser handles the structured Sample Data inputs.
# In a real scenario, this could use Document AI or further docling capabilities.

def extract_sales_orders_from_pdf(filepath: str):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        
    return text

def parse_csv_to_dict(filepath: str):
    import pandas as pd
    if not os.path.exists(filepath):
        return []
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")
