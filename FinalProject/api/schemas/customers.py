from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    email : str
    customer_name : str
    phone_num : str
    address : str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    email: Optional[str] = None
    customer_name: Optional[str] = None
    phone_num: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    class ConfigDict:
        from_attributes = True