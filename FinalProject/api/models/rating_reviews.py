from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class RatingReviews(Base):
    __tablename__ = "rating_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review = Column(String, nullable=False)
    score = Column(DECIMAL(5, 2), nullable=False)
