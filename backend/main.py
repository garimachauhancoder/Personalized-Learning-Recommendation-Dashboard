from fastapi import FastAPI
from sqlalchemy import text
from backend.database import engine

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