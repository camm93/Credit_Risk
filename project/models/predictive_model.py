from abc import ABC, abstractmethod


class PredictiveModel(ABC):

    MODEL_FILENAME = ''

    def __init__(self):
        self._load_model()

    @abstractmethod
    def predict(self) -> None:
        pass

    @abstractmethod
    def _load_model(self):
        pass

    @abstractmethod
    def _prepare_input():
        pass
