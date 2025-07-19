from fastapi import APIRouter
from crud.db_crud import read_data
import time

import psutil
import pandas as pd 
from datetime import datetime

import pytz
from pymongo import MongoClient

router = APIRouter()

keys = ['가명처리 단계', '측정 시간' ,'측정 시점', '전체 CPU 사용률', '사용중인 메모리', '전체 메모리 사용률']
performance = dict.fromkeys(keys)

kst = pytz.timezone('Asia/Seoul')

client = MongoClient("mongodb://localhost:27017/")
db = client.HEROS


@router.get('/first')
async def frist_preprocess():
    
    # 서버 상태 조회
    server_status = db.command("serverStatus")
    
    # 메모리 관련 정보 추출
    memory_info = server_status.get("mem", {})
    wired_tiger_info = server_status.get("wiredTiger", {}).get("cache", {})

    # 출력
    print("메모리 정보:")
    print(f" - Virtual Memory: {memory_info.get('virtual', 'N/A')} MB")
    print(f" - Resident Memory: {memory_info.get('resident', 'N/A')} MB")
    print(f" - Mapped Memory: {memory_info.get('mapped', 'N/A')} MB")

    print("\nWiredTiger 캐시 정보:")
    print(f" - 현재 캐시 사용량: {wired_tiger_info.get('bytes currently in the cache', 'N/A') / (1024**2):.2f} MB")
    print(f" - 최대 캐시 크기: {wired_tiger_info.get('maximum bytes configured', 'N/A') / (1024**2):.2f} MB")
    
    """""
    #전체 CPU 사용률(퍼센트)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"초기, 전체 CPU 사용률:{cpu_usage}")
    
    #시용 중인 메모리
    memory_info = psutil.virtual_memory()
    print(f"초기, 사용 중인 메모리: {memory_info.used / (1024**3):.2f} GB")
    print(f"초기, 메모리 사용률: {memory_info.percent}%")
    
    performance['가명처리 단계'] = '1'
    performance['측정 시간'] = datetime.now(kst)
    performance['측정 시점'] = '가명처리 전'
    performance['전체 CPU 사용률'] = cpu_usage
    performance['사용중인 메모리'] = memory_info.used / (1024**3)
    performance['전체 메모리 사용률'] = memory_info.percent
    
    df = pd.DataFrame(performance, index=[0])
    df.to_csv('performance_check.csv', encoding='cp949', mode='a', header=False, index=False)
    
    """""
    
    # 1. 시작 시간 기록
    start_time = time.time()
    print(f"[lever 1] Start time: {start_time}")

    # 2. 데이터 베이스 읽어오기
    data = await read_data()
    
    # 메모리 관련 정보 추출
    memory_info = server_status.get("mem", {})
    wired_tiger_info = server_status.get("wiredTiger", {}).get("cache", {})

    # 출력
    print("메모리 정보:")
    print(f" - Virtual Memory: {memory_info.get('virtual', 'N/A')} MB")
    print(f" - Resident Memory: {memory_info.get('resident', 'N/A')} MB")
    print(f" - Mapped Memory: {memory_info.get('mapped', 'N/A')} MB")

    print("\nWiredTiger 캐시 정보:")
    print(f" - 현재 캐시 사용량: {wired_tiger_info.get('bytes currently in the cache', 'N/A') / (1024**2):.2f} MB")
    print(f" - 최대 캐시 크기: {wired_tiger_info.get('maximum bytes configured', 'N/A') / (1024**2):.2f} MB")

    # 3. 종료 시간 기록
    #end_time = time.time()
   # print(f"[lever 1] End time: {end_time}")

    # 4. 실행 시간 계산
    #execution_time = end_time - start_time
    #print(f"[level 1] Execution time: {execution_time} seconds")
    
    #전체 CPU 사용률(퍼센트)
    #cpu_usage = psutil.cpu_percent(interval=1)
    #print(f"초기, 전체 CPU 사용률:{cpu_usage}")
    
    #시용 중인 메모리
    #memory_info = psutil.virtual_memory()
    #print(f"가명 처리 후, 사용 중인 메모리: {memory_info.used / (1024**3):.2f} GB")
    #print(f"가명 처리 후, 메모리 사용률: {memory_info.percent}%")
    
    #performance['측정 시간'] = datetime.now(kst)
    #performance['측정 시점'] = '가명처리 후'
    #performance['전체 CPU 사용률'] = cpu_usage
    #performance['사용중인 메모리'] = memory_info.used / (1024**3)
    #performance['전체 메모리 사용률'] = memory_info.percent
    
    
    #df = pd.DataFrame(performance, index=[0])
    #df.to_csv('performance_check.csv', encoding='cp949', mode='a', header=False, index=False)

    return  data