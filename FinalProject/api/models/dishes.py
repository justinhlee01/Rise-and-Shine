from sqlalchemy import Column, Integer, String, Text, DECIMAL
from ..dependencies.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), unique=True, nullable=False)  
    ingredients = Column(Text, nullable=False)                     
    calories = Column(Integer, nullable=False)                   
    food_catagories = Column(String(100), nullable=False)         
    price = Column(DECIMAL(6, 2), nullable=False)                 
