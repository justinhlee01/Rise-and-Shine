from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DishBase(BaseModel):
    dish_name: str
    ingredients: str
    calories: int
    food_catagories: str
    price: float


class DishCreate(DishBase):
    pass


class DishUpdate(BaseModel):
    dish_name: Optional[str] = None
    price: Optional[float] = None


class Dish(DishBase):
    id: int

    class ConfigDict:
        from_attributes = True