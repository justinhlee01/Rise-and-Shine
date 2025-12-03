from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..models import rating_reviews as model
from ..controllers import rating_reviews as controller
from ..schemas import rating_reviews as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Rating Reviews"],
    prefix="/rating-reviews"
)


@router.post("/", response_model=schema.RatingReviews)
def create(request: schema.RatingReviewsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.RatingReviews])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/by-dish/{dish_id}", response_model=list[schema.RatingReviews])
def get_reviews_for_dish(dish_id: int, db: Session = Depends(get_db)):
    return controller.read_dish(db=db, dish_id=dish_id)

@router.get("/{item_id}", response_model=list[schema.RatingReviews])
def get_reviews_for_dish(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.RatingReviews)
def update(item_id: int, request: schema.RatingReviewsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
