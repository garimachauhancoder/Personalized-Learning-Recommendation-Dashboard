from fastapi import fastapi

app = FastAPI(title="Personalised Learning Recommendation System")

@app.get("/")
def home():
    return {
        "message": "Personalised Learning API is running"
    }