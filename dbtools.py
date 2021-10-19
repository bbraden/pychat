from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://braden:1234@cluster0.w4snx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["chat"]["chat"]