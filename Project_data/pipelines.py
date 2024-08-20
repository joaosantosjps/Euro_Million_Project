import os
from pymongo import MongoClient
from Project_data.items import Database


class ProcessNumbersPipeline:
    connection_string = os.getenv("MONGODB_HOST")

    def connection(self):
        client = MongoClient(f"{self.connection_string}?authSource=admin")
        db = client["Euro_Million"]

        return db
    
    def create_collection(self, db):
        pass

    def process_item(self, item, spider):
        return item
    
    """def connection_Mongodb(self):
        client = MongoClient(f"{self.connection_string}?authSource=admin")
        db = client["Euro_Million"]
        collection = db.list_collection_names()

        if not "Draw_History" in collection:
            db.create_collection("Draw_History")"""
