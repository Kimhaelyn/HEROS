from pymongo.collection import Collection
from bson import ObjectId
from typing import Optional

#새 데이터 db에 추가 
def create_document(collection: Collection, doc: dict):
    
    result = collection.insert_one(doc)
    return str(result.inserted_id)

# 이전 데이터 가져오기 
def get_latest_document(collection: Collection):
    return collection.find_one(sort=[("datetime", -1)])


