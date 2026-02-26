from abc import ABC, abstractmethod


class BaseRecommender(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def train(self, x, y):
        pass

    @abstractmethod
    def predict(self, x):
        pass