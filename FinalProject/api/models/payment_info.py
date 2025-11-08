from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_detail_id = Column(Integer, ForeignKey("order_details.id"), unique=True, nullable=False)

    card_num = Column(Integer, nullable=False)
    cvv = Column(Integer, nullable=False)

    order_detail = relationship("OrderDetail", back_populates="payment_info", uselist=False)
