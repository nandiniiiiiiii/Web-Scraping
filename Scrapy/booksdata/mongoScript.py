from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://NandiniNegi:nandini123@cluster0.tuvn301.mongodb.net")

db = client.webscraping
collection = db.books

doc = post = {
    "author": "Nandini",
    "text" : "My first blog",
    "date" : datetime.datetime.utcnow(),
}

post_id = collection.insert_one(post).inserted_id
print(post_id)
