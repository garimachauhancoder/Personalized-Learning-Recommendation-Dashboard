from pydantic import BaseModel

class AssessmentCreate(BaseModel):
    user_id:int
    topic_id:int
    score:float
    total_questions:int
    correct_answers:int
    time_taken_minutes:int
    difficulty:str