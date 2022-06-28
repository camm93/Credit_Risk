

from predictive_model import PredictiveModel


class LogisticRegression(PredictiveModel):

    def __init__(self, filename: str):
        super().__init__(filename)

    def predict(self) -> None:
        return super().predict()

    def _load_model(self):
        return super().load_model()

    def _prepare_input():
        pass

    def _prepare_output():
        pass
