import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def connect(collection:str):
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client[os.getenv('MONGO_DB')]
    collections = db[collection]
    return client, collections

