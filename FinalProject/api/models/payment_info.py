from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)
    is_cash = Column(Boolean, nullable=False, server_default="0")
    card_num = Column(Integer, nullable=True)
    cvv = Column(Integer, nullable=True)

    order = relationship("Order", back_populates="payment_info")
