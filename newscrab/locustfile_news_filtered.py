import os
import random
from locust import HttpUser, task, between
from dotenv import load_dotenv
from datetime import datetime, timedelta

# .env 파일을 통해 AUTH_TOKEN을 불러오기 (필요하다면)
load_dotenv()

class WebsiteUser(HttpUser):
    # 기본 설정
    host = "https://newscrab.duckdns.org"
    wait_time = between(1, 1)
    
    auth_token = os.getenv("ACCESS_TOKEN")  # .env 파일에서 AUTH_TOKEN을 불러옴

    @task
    def filter_news(self):
        # industryId는 1에서 16 사이의 랜덤한 숫자
        industry_id = random.randint(1, 16)
        
        # de는 2024-08-27부터 오늘까지의 랜덤한 날짜
        start_date = datetime(2024, 8, 27)
        today = datetime.today()
        de = (start_date + timedelta(days=random.randint(0, (today - start_date).days))).strftime('%Y-%m-%d')
        
        # ds는 de보다 작은 날짜로 랜덤 설정 (de로부터 최대 30일 전)
        ds = (datetime.strptime(de, '%Y-%m-%d') - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
        
        # option은 'total', 'hot', 'scrap' 중 하나 랜덤 선택
        option = random.choice(['total', 'hot', 'scrap'])
        
        params = {
            "industryId": industry_id,
            "page": 1,
            "size": 10,
            "ds": ds,
            "de": de,
            "option": option
        }
        
        # GET 요청 보내기
        self.client.get("/api/v1/news/filter", 
                        params=params,
                        headers={"Authorization": f"Bearer {self.auth_token}"})
