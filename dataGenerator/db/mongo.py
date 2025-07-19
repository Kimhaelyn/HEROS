from pymongo import MongoClient

def connect_mongo():
    #docker에서
    #client = MongoClient("mongodb://admin:admin@mongodb:27017/HEROS?authSource=admin")
    client = MongoClient("mongodb://localhost:27017")
    db = client['HEROS']
    collection = db['people_data']

    return collection
