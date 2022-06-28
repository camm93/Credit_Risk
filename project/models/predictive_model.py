from abc import ABC, abstractmethod


class PredictiveModel(ABC):

    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def predict(self) -> None:
        pass

    @abstractmethod
    def _load_model(self):
        pass

    @abstractmethod
    def _prepare_input():
        pass

    @abstractmethod
    def _prepare_output():
        pass
