import joblib
from typing import Tuple
from models.enums import LoanStatus
from models.predictive_model import PredictiveModel


class RandomForest(PredictiveModel):

    CLASSIFIER_FILENAME = 'rf_loan_clas.joblib'
    REGRESSION_FILENAME = 'rf_score_reg.joblib'

    @property
    def regression_model(self):
        return self._reg_model

    @property
    def classification_model(self):
        return self._clas_model

    def predict(self, encoded_input: list) -> Tuple[str, str]:
        validated_data = RandomForest._prepare_input(encoded_input)
        print('validated_data1', validated_data)
        predicted_score = self.regression_model.predict(validated_data)
        print('predicted_score', predicted_score)
        score_output = RandomForest._prepare_output(predicted_score)
        loan_status = self._classify(predicted_score[0], encoded_input)
        return score_output, loan_status

    def _classify(self, score: float, encoded_input: list) -> str:
        print('encoded_input2', encoded_input)
        print(score)
        encoded_input.insert(0, score)
        encoded_input.insert(16, 3)
        validated_data = RandomForest._prepare_input(encoded_input)
        print('validated_data', validated_data)
        predicted_status = self.classification_model.predict(validated_data)
        status_output = RandomForest._prepare_classification_output(predicted_status)
        return status_output

    def _load_model(self) -> None:
        self._reg_model = joblib.load(self.REGRESSION_FILENAME)
        self._clas_model = joblib.load(self.CLASSIFIER_FILENAME)
        print("Se carga modelo entrenado.")

    @staticmethod
    def _prepare_classification_output(predicted_status) -> str:
        status = LoanStatus(predicted_status[0]).name.title().replace('_', ' ')
        return f'Your loan is more likely to be {status}.'

    @staticmethod
    def _prepare_input(form_data: list) -> list:
        print("prepare_input", form_data)
        return [form_data]

    @staticmethod
    def _prepare_output(predicted_score) -> str:
        return f"Your estimated score is: {predicted_score[0]:>.1f}"
