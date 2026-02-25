from locust import HttpUser, task, between


class GoProjectUser(HttpUser):

    wait_time = between(1, 3)

        # .........GET

    @task
    def load_count(self):
        self.client.get('/api/count')

        # .........POST

    @task
    def increment_counter(self):

        self.client.post('/api/increment')
