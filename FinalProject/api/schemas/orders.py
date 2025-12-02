from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class OrderBase(BaseModel):
    # Guest-friendly fields (no account required)
    customer_name: str
    customer_phone: str
    delivery_address: str
    order_type: str  # "takeout" or "delivery"

    # Optional stuff
    description: Optional[str] = None
    customer_email: Optional[str] = None  # link to account if they have one
    promo_code: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    description: Optional[str] = None
    promo_code: Optional[str] = None


class Order(OrderBase):
    id: int
    status: str
    order_date: datetime

    class ConfigDict:
        from_attributes = True
