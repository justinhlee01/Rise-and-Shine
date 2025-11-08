from sqlalchemy import Column, Integer, String, Date
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_num = Column(String(100), nullable=False)
    exp_date = Column(Date, nullable=False)
