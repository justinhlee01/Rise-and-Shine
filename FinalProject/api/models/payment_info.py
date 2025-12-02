from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    payment_type = Column(String(20), nullable=False)
    card_num = Column(Integer, nullable=True)
    cvv = Column(Integer, nullable=True)

    order = relationship("Order", back_populates="payment_info")
