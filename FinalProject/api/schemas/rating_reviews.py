from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RatingReviewsBase(BaseModel):
    review : str
    score : float


class RatingReviewsCreate(RatingReviewsBase):
    pass


class RatingReviewsUpdate(BaseModel):
    score: Optional[float] = None
    review: Optional[str] = None



class RatingReviews(RatingReviewsBase):
    id: int

    class ConfigDict:
        from_attributes = True