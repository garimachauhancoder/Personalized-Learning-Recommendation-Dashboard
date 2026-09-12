from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import User
from backend.schemas.user import UserCreate
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()
    
@router.post("/")
def create_user(
    user:UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        education_level=user.education_level
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user