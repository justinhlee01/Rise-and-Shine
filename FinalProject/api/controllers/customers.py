from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Customer(
        email=request.email,
        customer_name=request.customer_name,
        phone_num=request.phone_num,
        address=request.address,
        order_id=request.order_id,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return result


def read_one(db: Session, email: str):
    try:
        item = db.query(model.Customer).filter(
            model.Customer.email == email
        ).first()
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found!",
            )
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return item


def update(db: Session, email: str, request):
    try:
        item = db.query(model.Customer).filter(
            model.Customer.email == email
        )
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found!",
            )

        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )
    return item.first()


def delete(db: Session, email: str):
    try:
        item = db.query(model.Customer).filter(
            model.Customer.email == email
        )
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found!",
            )

        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
