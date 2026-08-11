import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "")

client = MongoClient(MONGO_URI) if MONGO_URI else None
db = client["sessionhack"] if client else None


def get_collection(name: str):
    if db is None:
        return None
    return db[name]


def insert(collection: str, data: dict):
    col = get_collection(collection)
    if col is not None:
        return col.insert_one(data)
    return None


def find(collection: str, query: dict):
    col = get_collection(collection)
    if col is not None:
        return list(col.find(query))
    return []


def update(collection: str, query: dict, data: dict):
    col = get_collection(collection)
    if col is not None:
        return col.update_one(query, {"$set": data})
    return None
