from evaluation.evaluate import evaluate


class ABExperiment:

    def __init__(self, model_a, model_b):
        self.model_a = model_a
        self.model_b = model_b

    def run(self, x, y):
        preds_a = self.model_a.predict(x)
        preds_b = self.model_b.predict(x)

        results_a = evaluate(y, preds_a.argsort(axis=1)[:, ::-1])
        results_b = evaluate(y, preds_b.argsort(axis=1)[:, ::-1])

        return {"A": results_a, "B": results_b}