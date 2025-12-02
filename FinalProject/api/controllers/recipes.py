from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import recipes as model
from ..models import dishes as dish_model
from ..models import resources as resource_model


def create(db: Session, request):
    """
    Create a new recipe row linking one dish to one resource (ingredient)
    with the amount of that ingredient needed for ONE dish.
    """

    # Optional but helpful: validate FK references
    dish = db.query(dish_model.Dish).filter(dish_model.Dish.id == request.dish_id).first()
    if not dish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish with id {request.dish_id} not found",
        )

    resource = (
        db.query(resource_model.Resource)
        .filter(resource_model.Resource.id == request.resource_id)
        .first()
    )
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resource with id {request.resource_id} not found",
        )

    new_item = model.Recipe(
        dish_id=request.dish_id,
        resource_id=request.resource_id,
        amount=request.amount,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return new_item


def read_all(db: Session):
    try:
        items = db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return items


def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!",
            )
    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return item


def update(db: Session, request, item_id: int):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!",
            )

        # Only update fields that were provided (all Optional in RecipeUpdate)
        if request.dish_id is not None:
            dish = (
                db.query(dish_model.Dish)
                .filter(dish_model.Dish.id == request.dish_id)
                .first()
            )
            if not dish:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Dish with id {request.dish_id} not found",
                )
            item.dish_id = request.dish_id

        if request.resource_id is not None:
            resource = (
                db.query(resource_model.Resource)
                .filter(resource_model.Resource.id == request.resource_id)
                .first()
            )
            if not resource:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Resource with id {request.resource_id} not found",
                )
            item.resource_id = request.resource_id

        if request.amount is not None:
            item.amount = request.amount

        db.commit()
        db.refresh(item)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return item


def delete(db: Session, item_id: int):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == item_id)
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!",
            )
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
