import os
from pymongo import MongoClient

class MongodbDatabase:
    connection_string = os.getenv("MONGODB_HOST")
        
    def connect_mongo(self):
        client = MongoClient(f"{self.connection_string}?authSource=admin")
        db = client["Euro_Million"]
        
        self.collection_create(db=db)

        return db
        
    def collection_create(self, db):
        collections = db.list_collection_names()

        if not "Draw_History" in collections:
            db.create_collection("Draw_History")
        
        collection = db["Draw_History"]

        return collection
