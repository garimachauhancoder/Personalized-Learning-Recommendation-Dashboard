from pydantic import BaseModel
from typing import Optional

class TopicCreate(BaseModel):
    name: str
    category: str | None = None
    description: str | None = None