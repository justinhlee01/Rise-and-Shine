from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    card_num: int
    cvv: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_num: Optional[int] = None
    cvv: Optional[int] = None


class Payment(PaymentBase):
    payment_id: int

    class ConfigDict:
        from_attributes = True
