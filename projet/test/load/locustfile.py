from locust import HttpUser, task, between

class GoProjectUser(HttpUser):
    wait_time = between(1, 3)
    @task
    def load_homepage(self):
        
        self.client.get("/api/count")
