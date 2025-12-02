from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as model
from ..models import recipes as recipe_model
from ..models import resources as resource_model
from sqlalchemy.exc import SQLAlchemyError
from typing import List


def create(db: Session, request):

    _check_inventory_for_dish(db, request.dish_id, request.amount)

    new_item = model.OrderDetail(
        order_id=request.order_id,
        dish_id=request.dish_id,
        amount=request.amount
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def _check_inventory_for_dish(db: Session, dish_id: int, quantity: int) -> None:
    """Raises HTTPException(400) if any ingredient is insufficient."""
    # All recipe rows for this dish (what ingredients it needs)
    recipes = db.query(recipe_model.Recipe).filter(
        recipe_model.Recipe.dish_id == dish_id
    ).all()

    if not recipes:
        # No recipe defined → treat as configuration error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No recipe found for this dish; cannot check inventory.",
        )

    insufficient = []

    for r in recipes:
        required = r.amount * quantity
        resource = db.query(resource_model.Resource).filter(
            resource_model.Resource.id == r.resource_id
        ).first()

        if resource is None:
            insufficient.append(
                {
                    "resource_id": r.resource_id,
                    "reason": "Ingredient not found in inventory.",
                }
            )
            continue

        if resource.amount < required:
            insufficient.append(
                {
                    "item": resource.item,
                    "have": resource.amount,
                    "need": required,
                }
            )

    if insufficient:
        # This is what your frontend / docs will describe as “alert”
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Insufficient ingredients to fulfill this order.",
                "missing": insufficient,
            },
        )

    # Optional: if everything is OK, reserve / decrement inventory here:
    for r in recipes:
        required = r.amount * quantity
        resource = db.query(resource_model.Resource).filter(
            resource_model.Resource.id == r.resource_id
        ).first()
        resource.amount -= required

    db.commit()
