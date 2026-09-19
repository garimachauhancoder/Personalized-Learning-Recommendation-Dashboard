from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Assessment
from backend.schemas.assessment import AssessmentCreate

router = APIRouter(
    prefix="/assessments",
    tags=["Assessments"]
)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_assessment(
    assessment: AssessmentCreate,
    db: Session = Depends(get_db)
):
    new_assessment = Assessment(
        user_id=assessment.user_id,
        topic_id=assessment.topic_id,
        score=assessment.score,
        total_questions=assessment.total_questions,
        correct_answers=assessment.correct_answers,
        time_taken_minutes=assessment.time_taken_minutes,
        difficulty=assessment.difficulty
    )

    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)

    return new_assessment

@router.get("/")
def get_assessments(db: Session = Depends(get_db)):
    assessments = db.query(Assessment).all()
    return assessments