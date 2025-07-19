from db.database import collection, check_data_exists
from typing import List
from model.mongo_model import Data


async def read_data():
    
    dataSet = []
    
    exists = await check_data_exists()
    if exists:
        print("yes data")
    else:
        print("no data")
    
    try:
        #count = await collection.count_documents({})
        #print(count, flush=True)
        
        
        async for data in collection.find({}):
            #print(Data(**data), flush=True)
            dataSet.append(Data(**data))
    
    except Exception as e:
        
        return {"error": str(e)}
    
    #print(dataSet, flush=True)
    
    return dataSet
    
        
    

