from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 1)  # 각 요청 사이의 대기 시간
    host = "https://newscrab.duckdns.org"

    @task
    def login_and_logout(self):


        # 로그인 요청 보내기
        login_response = self.client.post("/api/v1/user/login", json={"loginId": "ehdrjs1", "password": "Kk9169445@"})
        
        # 로그인 성공 여부 확인 (예: 200 상태 코드)
        if login_response.status_code == 200:
            # 로그아웃 요청 전에 대기 시간 추가
            time.sleep(1)  # 1초 대기
            
            # 2. 로그아웃 요청 보내기
            self.client.post("/api/v1/user/logout")