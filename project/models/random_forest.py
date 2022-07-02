import joblib
from models.predictive_model import PredictiveModel


class RandomForest(PredictiveModel):

    MODEL_FILENAME = ''

    @property
    def model(self):
        return self._model

    def predict(self):
        pass

    def _load_model(self):
        self._model = joblib.load(self.MODEL_FILENAME)

    @staticmethod
    def _prepare_input(form_data: list) -> list:
        pass

    def _prepare_output():
        pass
