from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from backend.database import Base
from sqlalchemy.dialects.postgresql import JSONB

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    education_level = Column(String(100))
    created_at= Column(DateTime, server_default=func.now())

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key= True)
    name = Column(String(100), nullable=False)
    category = Column(String(100))
    description = Column(String)

class LearningSession(Base):
    __tablename__ = "learning_sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, nullable=False)

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    duration_minutes = Column(Integer)
    resource_type = Column(String(50))
    resource_id = Column(Integer)

class Assessment(Base):
    __tablename__ = "assessments"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, nullable=False)
    score = Column(Float)
    total_questions = Column(Integer)
    correct_answers = Column(Integer)
    time_taken_minutes = Column(Integer)
    difficulty = Column(String(50))
    attempted_at = Column(
        DateTime,
        server_default = func.now()
    )

class LearningEvent(Base):
    __tablename__ = "learning_events"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    topic_id = Column(Integer)
    event_type = Column(String(100))
    timestamp = Column(
        DateTime,
        server_default=func.now()
    )
    event_metadata = Column(JSONB, name="metadata")