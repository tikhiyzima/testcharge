from locust import HttpUser, task

class AnonymousUser(HttpUser):
    @task
    def home_page(self):
        self.client.get("/")   

    @task
    def calendar_page(self):
        self.client.get("/calendrier.html")

    @task
    def portrait_page(self):
        self.client.get("/portrait.html")
