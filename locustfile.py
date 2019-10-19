from locust import HttpLocust, TaskSet
import lorem


def index(l):
    l.client.get("/tasks/")

def create(l):
    l.client.post("/tasks/", {"title": lorem.sentence()})

class UserBehavior(TaskSet):
    tasks = {index: 5, create: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

