from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    amount: float
    card_num: int
    cvv: int
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    card_num: Optional[int] = None
    cvv: Optional[int] = None


class Payment(PaymentBase):
    payment_id: int

    class ConfigDict:
        from_attributes = True
