from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.database import Base

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