from pydantic import BaseModel
from datetime import datetime

class LearningSessionCreate(BaseModel):
    user_id: int
    topic_id:int
    start_time: datetime | None = None
    end_time: datetime | None = None
    duration_minutes: int
    resource_type: str | None = None
    resource_id: int | None = None