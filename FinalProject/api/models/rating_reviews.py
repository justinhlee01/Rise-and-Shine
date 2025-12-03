from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class RatingReviews(Base):
    __tablename__ = "rating_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False, index=True)
    review = Column(String(255), nullable=False)
    score = Column(DECIMAL(5, 2), nullable=False)
    
    dish = relationship("Dish", back_populates="rating_reviews")

