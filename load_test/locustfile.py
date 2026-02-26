from locust import HttpUser, task, between
import random


class RecommenderUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def recommend(self):
        sequence = [random.randint(1, 1000) for _ in range(50)]
        self.client.post("/recommend", json=sequence)