from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promotion_num: str
    discount_percent: int
    exp_date: datetime


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotion_num: Optional[str] = None
    discount_percent: Optional[int] = None
    exp_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
