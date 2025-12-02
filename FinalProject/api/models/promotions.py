from sqlalchemy import func, Column, Integer, String, DateTime, Boolean, DateTime, DECIMAL
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_num = Column(String(50), unique=True, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    exp_date = Column(DateTime, nullable=False)
