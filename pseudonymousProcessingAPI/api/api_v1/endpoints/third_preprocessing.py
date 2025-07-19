from fastapi import APIRouter
from crud.db_crud import read_data
from api.api_v1.endpoints.second_preprocessing import second_preprocess
import time

import psutil
import pandas as pd 
from datetime import datetime
import pytz

router = APIRouter()

update_data = []
age = [0, 0, 0, 0]

keys = ['가명처리 단계', '측정 시간' ,'측정 시점', '전체 CPU 사용률', '사용중인 메모리', '전체 메모리 사용률']
performance = dict.fromkeys(keys)

kst = pytz.timezone('Asia/Seoul')

@router.get('/third')
async def second_preprocess():
    
    #전체 CPU 사용률(퍼센트)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"초기, 전체 CPU 사용률:{cpu_usage}")
    
    #시용 중인 메모리
    memory_info = psutil.virtual_memory()
    print(f"초기, 사용 중인 메모리: {memory_info.used / (1024**3):.2f} GB")
    print(f"초기, 메모리 사용률: {memory_info.percent}%")
    
    
    performance['가명처리 단계'] = '3'
    performance['측정 시간'] = datetime.now(kst)
    performance['측정 시점'] = '가명처리 전'
    performance['전체 CPU 사용률'] = cpu_usage
    performance['사용중인 메모리'] = memory_info.used / (1024**3)
    performance['전체 메모리 사용률'] = memory_info.percent
    
    
    df = pd.DataFrame(performance, index=[0])
    df.to_csv('performance_check.csv', encoding='cp949', mode='a', header=False, index=False)
    
    
    # 1. 시작 시간 기록
    start_time = time.time()
    print(f"[level 3] Start time: {start_time}", flush=True)
    
    # 2. 데이터 베이스 읽어오기
    data = await read_data()
    #print(data, flush=True)
    
    # 3. 사람 객체만 가져오기
    for privacy in data:
        privacy = privacy.dict()
        
        #전체 CPU 사용률(퍼센트)
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"가명처리 시, 전체 CPU 사용률:{cpu_usage}")
        
        #사용 중인 메모리
        memory_info = psutil.virtual_memory()
        print(f"가명처처리 시, 사용 중인 메모리: {memory_info.used / (1024**3):.2f} GB")
        print(f"가명처리 시, 메모리 사용률: {memory_info.percent}%")
        
        
        performance['가명처리 단계'] = '3'
        performance['측정 시간'] = datetime.now(kst)
        performance['측정 시점'] = '가명처리 중'
        performance['전체 CPU 사용률'] = cpu_usage
        performance['사용중인 메모리'] = memory_info.used / (1024**3)
        performance['전체 메모리 사용률'] = memory_info.percent
        
        
        df = pd.DataFrame(performance, index=[0])
        df.to_csv('performance_check.csv',encoding='cp949', mode='a', header=False, index=False)
        
        for cell in privacy['cells']:
            #4. age_distribution 삭제
            del cell['age_distribution']
            
            #5. age_distribution 추가 
            cell['age_distribution'] ={
                "youth": 0,
                "middle_aged": 0,
                "senior": 0, 
                "elderly": 0
            }

            #6. 2단계 가명 처리 
            for person in cell['people']:
                
                # 7. IMSI 정보 지우기, 전화번호 지우기, 성별 지우기
                del person['mobile_number']
                del person['IMSI']
                del person['gender']
                
                # 8. 나이 가명 처리
                if person['age'] > 20 and person['age'] <30 :
                    person['age'] = 'mid_20s'
                    age[0]+=1
                
                elif person['age'] > 30 and person['age'] < 40 :
                    person['age'] = 'mid_30s'
                    age[0]+=1

                elif person['age'] > 40 and person['age'] < 50 :
                    person['age'] = 'mid_40s'
                    age[1]+=1

                elif person['age'] > 50 and person['age'] < 60 :
                    person['age'] = 'mid_50s'
                    age[2]+=1

                elif person['age'] > 60 and person['age'] < 70 :
                    person['age'] = 'mid_60s'
                    age[3]+=1
                
                elif person['age'] > 70:
                    person['age'] = 'mid_70s'
                    age[3]+=1
                
            # 9. 나이 분포 업데이트
            cell['age_distribution']['youth'] = age[0]
            cell['age_distribution']['middle_aged'] = age[1]
            cell['age_distribution']['senior'] = age[2]
            cell['age_distribution']['elderly'] = age[3]
        
        update_data.append(privacy) 
        
    # 10. 종료 시간 기록
    end_time = time.time()
    print(f"[level 3] End time: {end_time}", flush=True)

    # 11. 실행 시간 계산
    execution_time = end_time - start_time
    print(f"[level 3] Execution time: {execution_time} seconds", flush=True)
    
    #전체 CPU 사용률(퍼센트)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"가명 처리 후, 전체 CPU 사용률:{cpu_usage}")
    
    #시용 중인 메모리
    memory_info = psutil.virtual_memory()
    print(f"가명 처리 후, 사용 중인 메모리: {memory_info.used / (1024**3):.2f} GB")
    print(f"가명 처리 후, 메모리 사용률: {memory_info.percent}%")
    
    performance['가명처리 단계'] = '3'
    performance['측정 시간'] = datetime.now(kst)
    performance['측정 시점'] = '가명처리 후'
    performance['전체 CPU 사용률'] = cpu_usage
    performance['사용중인 메모리'] = memory_info.used / (1024**3)
    performance['전체 메모리 사용률'] = memory_info.percent
    
    
    df = pd.DataFrame(performance, index=[0])
    df.to_csv('performance_check.csv', encoding='cp949', mode='a', header=False, index=False)
    
    
    return update_data