class Trainer:

    def __init__(self, model):
        self.model = model

    def fit(self, x, y):
        return self.model.train(x, y)

    def inference(self, x):
        return self.model.predict(x)