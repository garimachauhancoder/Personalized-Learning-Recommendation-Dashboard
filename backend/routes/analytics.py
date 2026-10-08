from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database import SessionLocal
from backend.models import Assessment, Topic

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

@router.get("/user/{user_id}/topics")
def get_topic_performance(
    user_id: int,
    db: Session = Depends(get_db)
):
    results = (
        db.query(
            Assessment.topic_id,
            Topic.name,
            func.avg(Assessment.score).label("average_score"),
            func.count(Assessment.id).label("assessment_count")
        )
        .join(Topic, Assessment.topic_id == Topic.id)
        .filter(Assessment.user_id == user_id)
        .group_by(Assessment.topic_id, Topic.name)
        .all()
    )
    return [
        {
            "topic_id": topic_id,
            "topic": topic_name,
            "average_score": round(float(average_score), 2),
            "assessment_count": assessment_count
        }
        for topic_id, topic_name, average_score, assessment_count in results
    ]