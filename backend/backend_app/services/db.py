import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URL)
db = client["DeepStrike-Analytics"]