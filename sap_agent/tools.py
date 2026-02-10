import os
import pandas as pd
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Sample Data')

def fetch_sap_export(inv_number: str) -> dict:
    """Fetches details for a specific invoice number from the SAP export CSV."""
    filepath = os.path.join(DATA_DIR, "File5-SAP-Transactional-Export.csv")
    if not os.path.exists(filepath):
        return {"error": "SAP export file not found"}
        
    df = pd.read_csv(filepath)
    # NaN and formatting cleanup
    df = df.replace({np.nan: None})
    
    row = df[df['Reference Document Number VBAK-XBLNR'].astype(str) == str(inv_number)]
    if not row.empty:
        return row.iloc[0].to_dict()
    return {"error": f"Invoice {inv_number} not found in SAP"}

def check_prior_credits(inv_number: str) -> dict:
    """Checks if a sales order / invoice has any prior credits to prevent duplicates."""
    filepath = os.path.join(DATA_DIR, "File6-Prior-Credit-History-Log.csv")
    if not os.path.exists(filepath):
        return {"error": "Prior Credit History file not found"}
        
    df = pd.read_csv(filepath)
    # NaN and formatting cleanup
    df = df.replace({np.nan: None})
    
    row = df[df['Original_SO_ID'].astype(str) == str(inv_number)]
    if not row.empty:
        return {"has_prior_credit": True, "details": row.iloc[0].to_dict()}
    return {"has_prior_credit": False}
