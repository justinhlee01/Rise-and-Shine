from sqlalchemy import Column, Integer, String, Text, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), unique=True, nullable=False)                            
    food_catagory = Column(String(100), nullable=False)         
    price = Column(DECIMAL(6, 2), nullable=False)      

    recipes = relationship("Recipe", back_populates="dish", cascade="all, delete-orphan")
    order_details = relationship("OrderDetail", back_populates="dish")           
