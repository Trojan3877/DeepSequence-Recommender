from locust import HttpUser, task, between
import random


class DeepSequenceUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def recommend(self):
        sequence = [random.randint(1, 5000) for _ in range(50)]
        self.client.post("/recommend/123", json=sequence)