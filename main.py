from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://my-mongo-mongodb.default.svc.cluster.local:27017")
db = client.mydatabase

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.get("/items/")
def read_items():
    items = db.items.find()
    return {"items": list(items)}

