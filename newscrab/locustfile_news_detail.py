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
    def news_detail(self):

        news_id = random.randint(1, 2400)  # 1부터 2400 사이의 랜덤 뉴스 ID 선택

        # GET 요청으로 뉴스 상세정보 가져오기
        self.client.get(f"/news/{news_id}", 
                        headers={"Authorization": f"Bearer {self.auth_token}"})
