from db.mongo import connect_mongo
from crud.people_data import * 
from utils.make_new_doc import * 

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    
    collection = connect_mongo()
    
    #이전 문서 가져오기 
    prev_doc = get_latest_document(collection)
    
    #이전문서 바탕으로 새 문서 만들기 
    new_doc = create_next_document(prev_doc)
    
    #새 문서 db에 넣기
    result = create_document(collection, new_doc)
    
    logging.info(result)
    
    
#로컬에서 테스트할때    
if __name__ == "__main__":
    main()