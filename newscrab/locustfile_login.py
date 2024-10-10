from locust import HttpUser, task, constant

class MyUser(HttpUser):
    wait_time = constant(20) 
    host = "https://newscrab.duckdns.org"

    @task
    def login(self):

        # 로그인 요청 보내기
        login_response = self.client.post("/api/v1/user/login", json={"loginId": "ehdrjs1", "password": "Kk9169445@"})
        
