from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Customers"],
    prefix="/customers",
)


@router.post("/", response_model=schema.Customer)
def create(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Customer])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{email}", response_model=schema.Customer)
def read_one(email: str, db: Session = Depends(get_db)):
    return controller.read_one(db, email=email)


@router.put("/{email}", response_model=schema.Customer)
def update(email: str, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, email=email)


@router.delete("/{email}")
def delete(email: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, email=email)
