import joblib
from predictive_model import PredictiveModel


class RandomForest(PredictiveModel):

    def __init__(self, filename: str):
        super().__init__(filename)

    @property
    def model(self):
        return self._model

    def predict(self):
        pass

    def _load_model(self):
        model = open(self.filename, 'rb')
        self._model = joblib.load(model)

    def _prepare_input():
        pass

    def _prepare_output():
        pass
