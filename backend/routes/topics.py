from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Topic
from backend.schemas.topic import TopicCreate

router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_topic(
    topic_data: TopicCreate,
    db: Session = Depends(get_db)
):
    new_topic = Topic(
        name=topic_data.name,
        category=topic_data.category,
        description=topic_data.description
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic

@router.get("/")
def get_topics(db: Session = Depends(get_db)):
    topics = db.query(Topic).all()

    return topics