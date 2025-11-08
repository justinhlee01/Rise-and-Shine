from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    email = Column(String, primary_key=True, index=True, unique=True, nullable=False)
    customer_name = Column(String, nullable=False)
    phone_num = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))


    order = relationship("Order", back_populates="Customer")

    # test
