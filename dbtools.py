from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://braden:<password>@cluster0.w4snx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["chat"]["chat"]
