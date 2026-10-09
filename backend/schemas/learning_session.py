from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LearningSessionCreate(BaseModel):
    user_id: int
    topic_id:int
    start_time: datetime | None = None
    end_time: datetime | None = None
    duration_minutes: int
    resource_type: str | None = None
    resource_id: int | None = None

class LearningSessionResponse(BaseModel):
    id: int
    user_id: int
    topic_id: int
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    resource_type: Optional[str] = None
    resource_id: Optional[int] = None

    model_config = ConfigDict(from_attributes = True)