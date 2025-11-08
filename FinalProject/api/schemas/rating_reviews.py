from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RatingReviewsBase(BaseModel):
    review : str
    score : int


class RatingReviewsCreate(RatingReviewsBase):
    pass


class RatingReviewsUpdate(BaseModel):
    score: Optional[int] = None
    review: Optional[str] = None



class RatingReviews(RatingReviewsBase):
    id: int

    class ConfigDict:
        from_attributes = True