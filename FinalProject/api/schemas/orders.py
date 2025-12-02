from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_email: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_email: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: datetime = None

    class ConfigDict:
        from_attributes = True
