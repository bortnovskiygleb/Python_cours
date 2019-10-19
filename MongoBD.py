from pymongo import MongoClient
from pprint import pprint


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://Gleb:1234@cluster0-jrmok.mongodb.net/test?retryWrites=true&w=majority")


connection = Connect.get_connection()

db = connection.test

db.inventory.insert_one(
    {"item": "canvas",
     "qty": 1000,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})

cursor = db.inventory.find({})

for inventory in cursor:
    pprint(inventory)

cursor = db.inventory.find({"size.h": 28})
print('--------------------------')
for inventory in cursor:
    pprint(inventory)

db.inventory.delete_many({"qty": 1000})
cursor = db.inventory.find({"size.h": 28})
print('--------------------------')
for inventory in cursor:
    pprint(inventory)
