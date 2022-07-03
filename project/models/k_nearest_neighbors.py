from models.predictive_model import PredictiveModel


class KNearestNeighbors(PredictiveModel):

    def __init__(self, filename: str):
        super().__init__(filename)
        self._load_model()

    @property
    def model(self):
        return self._model

    def predict(self) -> None:
        validated_data = self._prepare_input()
        prediction = self._model.predict(validated_data)
        self._prepare_output(prediction)

    def _load_model(self):
        self._model = 'jpña' #models.load_model(self.filename)

    def _prepare_input():
        pass

    def _prepare_output():
        pass
