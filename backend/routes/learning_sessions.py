from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.learning_session import LearningSessionCreate
from backend.models import LearningSession
from backend.database import SessionLocal

router = APIRouter(
    prefix="/learning-sessions",
    tags=["Learning Sessions"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_learning_session(
    session: LearningSessionCreate,
    db: Session = Depends(get_db)
):
    new_session = LearningSession(
        user_id=session.user_id,
        topic_id=session.topic_id,
        start_time=session.start_time,
        end_time=session.end_time,
        duration_minutes=session.duration_minutes,
        resource_type=session.resource_type,
        resource_id=session.resource_id
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session

@router.get("/")
def get_learning_sessions(db: Session = Depends(get_db)):
    sessions = db.query(LearningSession).all()

    return sessions