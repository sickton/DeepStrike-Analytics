from fastapi import FastAPI
from backend.backend_app.routes import teams, players, analytics

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DeepStrike Analytics backend is running!"}

app.include_router(teams.router)
app.include_router(players.router)
app.include_router(analytics.router)
