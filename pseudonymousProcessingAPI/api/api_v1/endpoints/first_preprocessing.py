from fastapi import APIRouter
from crud.db_crud import read_data
import time

router = APIRouter()


@router.get('/first')
async def frist_preprocess():
    # 1. 시작 시간 기록
    start_time = time.time()
    print(f"[lever 1] Start time: {start_time}")

    # 2. 데이터 베이스 읽어오기
    data = await read_data()

    # 3. 종료 시간 기록
    end_time = time.time()
    print(f"[lever 1] End time: {end_time}")

    # 4. 실행 시간 계산
    execution_time = end_time - start_time
    print(f"[level 1] Execution time: {execution_time} seconds")

    return  data