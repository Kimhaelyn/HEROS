from bson import ObjectId
from typing import Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

import pymongo


client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["HEROS"]
collection = db["peopel_data"]

async def check_data_exists():
    
    count = await collection.count_documents({})
    
    return count > 0 