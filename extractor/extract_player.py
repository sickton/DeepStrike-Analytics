import os
import requests
from pymongo import MongoClient

API_KEY = os.getenv("API_FOOTBALL_KEY")
HEADERS = {"x-apisports-key": API_KEY}

url = "https://v3.football.api-sports.io/teams"
params = {"league": 39, "season": 2025}
response = requests.get(url, headers = HEADERS, params = params).json()

teams = []
for x in response["response"]:
    t = x["team"]
    v = x["venue"]

    teams.append({
        "id": t["id"],
        "name": t["name"],
        "logo": t["logo"],
        "venue": {
            "name": v["name"],
            "city": v["city"],
            "capacity": v["capacity"]
        }
    })

client = MongoClient("mongodb://localhost:27017/")
db = client["DeepStrike-Analytics"]
collection = db["Teams"]

collection.delete_many({})
collection.insert_many(teams)

print("All the teams updated successfully!")

playerCollection = db["Players"]
playerCollection.delete_many({})

for team in teams:
    id = team["id"]
    name = team["name"]

    squadUrl = f"https://v3.football.api-sports.io/players/squads?team={id}"
    sResponse = requests.get(squadUrl, headers = HEADERS).json()

    players = sResponse["response"][0]["players"]

    for p in players:
        playerDoc = {
            "id": p["id"],
            "name": p["name"],
            "age": p["age"],
            "positions": p["position"],
            "photo": p["photo"],
            "team_id": id,
            "team_name": name
        }

        playerCollection.insert_one(playerDoc)

    print(f"Players inserted for team:-{name}")

print("All premier league registered players inserted!")