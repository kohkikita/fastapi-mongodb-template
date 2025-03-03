from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:Test1234@cluster0.b9f4w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]