from typing import List, Optional
from pydantic import BaseModel, Field

class CreditRequestItem(BaseModel):
    so_number: str = Field(description="Sales Order Number")
    material: str = Field(description="Product affected / Material Number")
    inv_date: str = Field(description="Invoice Date")
    inv_number: str = Field(description="Invoice Number")
    inv_amount: float = Field(description="Invoice Amount")
    currency: str = Field(description="Currency used")

class ZMemoRow(BaseModel):
    sales_order_id: str
    material_number: str
    credit_amount: float
    currency: str
    reason_code: str
    approval_level: str

class CreditRequestData(BaseModel):
    ticket_number: str
    description: str
    items: List[CreditRequestItem]
    validation_status: str = "PENDING"
    validation_reason: Optional[str] = None
    total_credit_requested: float = 0.0
    zmemo_rows: List[ZMemoRow] = []

    class Config:
        arbitrary_types_allowed = True
