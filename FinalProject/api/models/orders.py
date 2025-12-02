from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_name = Column(String(255), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    delivery_address = Column(String(255), nullable=False)

    # "takeout" or "delivery"
    order_type = Column(String(20), nullable=False)

    # optional link to registered customer
    customer_email = Column(String(255), ForeignKey("customers.email"), nullable=True)

    status = Column(String(20), nullable=False, default="pending")
    order_date = Column(DateTime, nullable=False, default=datetime.now)
    description = Column(String(300), nullable=True)
    promo_code = Column(String(50), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    payment_info = relationship("PaymentInfo", back_populates="order", uselist=False)

    customer = relationship("Customer", back_populates="orders", foreign_keys=[customer_email])
