from fastapi import FastAPI
from sqlalchemy import text
from backend.database import engine
from backend.routes.users import router as users_router
from backend.routes.topics import router as topics_router
from backend.routes.learning_sessions import router as learning_sessions_router
from backend.routes.assessments import router as assessments_router
from backend.routes.learning_events import router as learning_events_router

app = FastAPI(title="Personalised Learning Recommendation System")

@app.get("/")
def home():
    return {
        "message": "Personalised Learning API is running"
    }

@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "database_connected": result.scalar() == 1
        }

app.include_router(users_router)
app.include_router(topics_router)
app.include_router(learning_sessions_router)
app.include_router(assessments_router)
app.include_router(learning_events_router)