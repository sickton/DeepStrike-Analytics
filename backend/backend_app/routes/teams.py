from fastapi import APIRouter
from backend.backend_app.services.db import db

router = APIRouter()

@router.get("/teams")
def get_teams():
    teams = list(db.Teams.find({}, {"_id": 0}))
    return teams