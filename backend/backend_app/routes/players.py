from fastapi import APIRouter
from backend.backend_app.services.db import db

router = APIRouter()

@router.get("/players")
def get_players():
    players = list(db.Players.find({}, {"_id": 0}))
    return players
