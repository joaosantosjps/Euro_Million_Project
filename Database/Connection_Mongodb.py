import os
from pymongo import MongoClient


CONNECTION_STRING = os.getenv("MONGODB_HOST")

client = MongoClient(f"{CONNECTION_STRING}?authSource=admin")
db = client["Euro_Million"]
collections = db.list_collection_names()

if not "Draw_History" in collections:
    db.create_collection("Draw_History")

items = {
    'draw_date': 'Sexta-feira 7 de abril de 2023',
 'lottery_numbers': ['5', '26', '28', '36', '46'],
 'raffle_stars': ['6', '12']
 }

items['lottery_numbers'] = [int(num) for num in items['lottery_numbers']]
items['raffle_stars'] = [int(num) for num in items['raffle_stars']]

collection = db["Draw_History"]
collection.insert_one(dict(items))
print(collection)