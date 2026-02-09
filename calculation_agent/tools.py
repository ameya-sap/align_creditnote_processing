
def calculate_discount(net_amount: float, discount_percent: float) -> float:
    """Calculates the absolute discount amount based on a percentage (e.g., 55 for 55%)."""
    return round(net_amount * (discount_percent / 100.0), 2)

def generate_zmemo_csv(rows: list[dict]) -> str:
    """
    Takes a list of dictionaries representing ZMEMO rows and writes them to a CSV.
    Returns the path to the generated CSV.
    """
    import pandas as pd
    import os
    if not rows:
        return "No rows provided to generate ZMEMO."
    df = pd.DataFrame(rows)
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_zmemo.csv")
    df.to_csv(out_path, index=False)
    return f"ZMEMO CSV generated at {out_path}"
