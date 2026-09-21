from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database import SessionLocal
from backend.models import Assessment

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.get("/user/{user_id}")
def get_user_analytics(
    user_id: int,
    db: Session = Depends(get_db)
):
    average_score = (
        db.query(func.avg(Assessment.id))
        .filter(Assessment.user_id == user_id)
        .scalar()
    )
    assessment_count = (
        db.query(func.count(Assessment.score))
        .filter(Assessment.user_id == user_id)
        .scalar()
    )
    return {
        "user_id":user_id,
        "average_score":average_score,
        "assessment_count":assessment_count
    }