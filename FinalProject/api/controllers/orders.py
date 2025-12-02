from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status, Response, Depends
from datetime import date, datetime
from ..models import payment_info as payment_model
from ..models import orders as model
from ..models import customers as customer_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Order(
        customer_name=request.customer_name,
        customer_phone=request.customer_phone,
        delivery_address=request.delivery_address,
        order_type=request.order_type,
        customer_email=request.customer_email,
        description=request.description,
        status="pending",
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session, start_date: date | None = None, end_date: date | None = None):
    q = db.query(model.Order)
    try:
        if start_date:
            q = q.filter(model.Order.order_date >= datetime.combine(start_date, datetime.min.time()))
        if end_date:
            q = q.filter(model.Order.order_date <= datetime.combine(end_date, datetime.max.time()))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return q.all()


def read_one(db: Session, order_id: int):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order


# join payments with orders for a given date
def daily_revenue(db: Session, target_date: date):
    start = datetime.combine(target_date, datetime.min.time())
    end = datetime.combine(target_date, datetime.max.time())

    total = (
        db.query(func.coalesce(func.sum(payment_model.PaymentInfo.amount), 0))
        .join(model.Order, payment_model.PaymentInfo.order_id == model.Order.id)
        .filter(model.Order.order_date >= start, model.Order.order_date <= end)
        .scalar()
    )

    return {"date": target_date.isoformat(), "total_revenue": float(total)}


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
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
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
