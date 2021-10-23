import lorem
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def index(self):
        self.client.get("/tasks/")

    @task(1)
    def create(self):
        self.client.post("/tasks/", {"title": lorem.sentence()})
