import os
from pymongo import MongoClient


CONNECTION_STRING = os.getenv("MONGODB_HOST")

client = MongoClient(f"{CONNECTION_STRING}?authSource=admin")
db = client["Euro_Million"]
collection = db.list_collection_names()
print(collection)

if not "Draw_History" in collection:
    db.create_collection("Draw_History")
    print("A coleção 'numbers' foi criada.")

else:
    print(f"A coleção {collection} já existe.")
