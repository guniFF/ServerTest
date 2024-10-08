import os
from locust import HttpUser, task, between
from dotenv import load_dotenv

# .env 파일 불러오기
load_dotenv()

class WebsiteUser(HttpUser):
    host = "https://newscrab.duckdns.org"

    wait_time = between(1,5)
    auth_token = os.getenv("ACCESS_TOKEN")  # .env에서 AUTH_TOKEN 불러오기

    @task
    def get_news(self):
        # GET 요청으로 뉴스 목록 가져오기
        self.client.get("/api/v1/news/recommend/list",
        headers={"Authorization": f"Bearer {self.auth_token}"})

    # @task
    # def post_scrap(self):
    #     # GET 요청으로 이미 스크랩된 뉴스 확인
    #     response = self.client.get("/api/v1/scrap", headers={"Authorization": f"Bearer {self.auth_token}"})
    #     if response.status_code == 200:
    #         # 이미 스크랩된 newsId 목록 가져오기
    #         scrapped_news_ids = [scrap['newsId'] for scrap in response.json()]

    #         # 아직 스크랩되지 않은 newsId 중에서 선택
    #         possible_news_ids = [news_id for news_id in range(1, 936) if news_id not in scrapped_news_ids]
            
    #         if possible_news_ids:
    #             random_news_id = random.choice(possible_news_ids)
                
    #             # POST 요청으로 뉴스 스크랩하기
    #             self.client.post("/api/v1/scrap", json={
    #                 "newsId": random_news_id,
    #                 "comment" : "locust 가 스크랩했어요 코멘트",
    #                 "scrapSummary" : "locust 가 스크랩했어요 설명",
    #                 "highlights" : [
    #                     {
    #                         "startPos" : 1,
    #                         "endPos" : 5,
    #                         "color" : "R"
    #                     },
    #                     {
    #                         "startPos" : 10,
    #                         "endPos" : 52,
    #                         "color" : "G"
    #                     }
    #                 ]
    #             }, headers={"Authorization": f"Bearer {self.auth_token}"})