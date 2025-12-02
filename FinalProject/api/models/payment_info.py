from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)

    customer_email = Column(String(255), ForeignKey("customers.email"), nullable=False)

    card_num = Column(Integer, nullable=False)
    cvv = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="payment_info", uselist=False)
