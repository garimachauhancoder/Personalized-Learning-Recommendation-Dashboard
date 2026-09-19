from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import LearningEvent
from backend.schemas.learning_event import LearningEventCreate

router = APIRouter(
    prefix="/learning_events",
    tags=["Learning Events"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_learning_event(
    event: LearningEventCreate,
    db: session = Dependss(get_db)
):
    new_event = LearningEvent(
        user_id=event.user_id,
        topic_id=event.topic_id,
        event_type=event.event_type,
        metadata=event.metadata
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("/")
def get_learning_events(
    db: Session = Depends(get_db)
):
    events = db.query(LearningEvent).all()
    return events

