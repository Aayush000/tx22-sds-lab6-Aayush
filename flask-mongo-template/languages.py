import pymongo

client = pymongo.MongoClient("mongodb+srv://Aayush:GNIUkwdOXo8KmZ1c@flaskmangodb.2bhda.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.database

db.create_collection('languages')

