from fastapi import APIRouter
from backend.backend_app.services.db import db

router = APIRouter()

@router.get("/analytics/age-distribution")
def age_distribution():
    players = list(db.Players.find({}, {"_id": 0, "age": 1}))

    age_groups = {
        "16-20": 0,
        "21-24": 0,
        "25-28": 0,
        "29-32": 0,
        "33-37": 0,
        "38+": 0
    }

    for p in players:
        age = p.get("age")
        if not age:
            continue
        if 16 <= age <= 20:
            age_groups["16-20"] += 1
        elif 21 <= age <= 24:
            age_groups["21-24"] += 1
        elif 25 <= age <= 28:
            age_groups["25-28"] += 1
        elif 29 <= age <= 32:
            age_groups["29-32"] += 1
        elif 33 <= age <= 37:
            age_groups["33-37"] += 1
        else:
            age_groups["38+"] += 1

    return age_groups
