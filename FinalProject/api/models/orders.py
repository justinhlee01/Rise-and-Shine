from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_name = Column(String(255), nullable=False)
    customer_phone = Column(String(20), nullable=False)

    customer_email = Column(String(255), ForeignKey("customers.email"), nullable=True)
    delivery_address = Column(String(255), nullable=True)
    order_type = Column(String(20), nullable=False)

    order_date = Column(DateTime, nullable=False, default=datetime.now)
    subtotal = Column(DECIMAL(8, 2), nullable=True)

    promo_code = Column(String(50), nullable=True)
    description = Column(String(255), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    customer = relationship("Customer", back_populates="orders", foreign_keys=[customer_email])
    payment_info = relationship("PaymentInfo", back_populates="order", uselist=False)
