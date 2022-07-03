from enum import Enum
import pandas as pd
from models.enums import LoanRiskGrade, PredictionModel


def feature_list(enum: Enum) -> tuple[list, list]:
    readable_features = [feature.value for feature in enum]
    if enum is LoanRiskGrade:
        orig_features = [feature.name for feature in enum]
        return orig_features, readable_features
    orig_features = [feature.name.lower() for feature in enum]
    return orig_features, readable_features

def feature_equivalence(enum: Enum) -> list[dict]:
    orig_features, readable_features = feature_list(enum)
    return [{'label': readable, 'value': orig} for orig, readable in zip(orig_features, readable_features)]

def model_list() -> list:
    return [model.value for model in PredictionModel]

def read_feather_db(file_name: str='mini_db.feather') -> pd.DataFrame:
    df = pd.read_feather(file_name)
    return df
