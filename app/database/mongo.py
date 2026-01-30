from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27017"
DB_NAME = "reading_tracker"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

collection = db["logs"]
