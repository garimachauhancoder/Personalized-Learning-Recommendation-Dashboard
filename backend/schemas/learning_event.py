from pydantic import BaseModel
from typing import Any

class LearningEventCreate(BaseModel):
    user_id: int
    topic_id: int
    event_type: str
    metadata: dict[str, Any] | None = None
