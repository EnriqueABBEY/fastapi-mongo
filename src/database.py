# src/db.py
from pymongo import MongoClient
import os

# Remplacez par l'URI de votre base de données
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://app_mongo:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "pets")

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

def get_database():
    return db
