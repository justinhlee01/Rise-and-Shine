from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_name : str
    phone_num : int
    address : str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_num: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    email: str

    class ConfigDict:
        from_attributes = True