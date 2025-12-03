from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), unique=True, nullable=False)                            
    food_category = Column(String(100), nullable=False)         
    price = Column(DECIMAL(6, 2), nullable=False)
    is_vegetarian = Column(Boolean, nullable=False, server_default="0")      

    recipes = relationship("Recipe", back_populates="dish")
    order_details = relationship("OrderDetail", back_populates="dish")        
    rating_reviews = relationship("RatingReviews", back_populates="dish")   
