def calculate_discount(net_amount: float, discount_percent: float) -> float:
    """Calculates the absolute discount amount based on a percentage (e.g., 55 for 55%)."""
    return round(net_amount * (discount_percent / 100.0), 2)

def generate_zmemo_csv(rows: list[dict]) -> str:
    """
    Takes a list of dictionaries representing ZMEMO rows and writes them to a CSV.
    The list must conform to the 29-column SAP format.
    Returns the path to the generated CSV.
    """
    import pandas as pd
    import os
    if not rows:
        return "No rows provided to generate ZMEMO."
    
    # Define exact columns in order
    columns = [
        "Serial #", "Sales Document Type VBAK-AUART", "Sales Organization VBAK-VKORG", 
        "Distribution Channel VBAK-VTWEG", "Division VBAK-SPART", "Reference Billing Document", 
        "Customer PO number VBKD-BSTKD", "Sold-to party KUAGV-KUNNR", "Bill to Party (NEW)", 
        "Ship-to party KUWEV-KUNNR", "Billing date VBKD-FKDAT MM/DD/AAAA", 
        "Services rendered date VBKD-FBUDA", "Material Number RV45A-MABNR(01)", "Posnr", 
        "Quantity VBAP-ZMENG(01)", "Units VRKME", "Plant VBAP-WERKS(01)", 
        "ZPR0 KOMV-KBETR(02)", "Order reason VBAK-AUGRU", "Document Currency VBAK-WAERK", 
        "Assignment number VBAK-ZUONR", "Form Header", "Form Header One", 
        "Reference Document Number VBAK-XBLNR", "Patient ID ZAVBAK-ZZPATIENT", 
        "SFDC Ticket Number ZAVBAK-ZZSFDC_TKT", "SAGA Contract Number", 
        "Treatment Option", "Deliverable Type"
    ]
    
    df = pd.DataFrame(rows, columns=columns)
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_zmemo.csv")
    df.to_csv(out_path, index=False)
    return f"ZMEMO CSV generated at {out_path}"
