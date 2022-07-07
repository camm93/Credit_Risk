from enum import Enum
from typing import Dict, List, Union
from matplotlib.figure import Figure
import pandas as pd

from enums import CategoricalFeature, NumericalFeature
from models import RandomForest
from models.enums import LoanPurpose, LoanTerm, PredictionModel
from plots import create_boxplot, create_histogram, create_heatmap
from services.utils import feature_list


def get_user_stats():
    return {
        "Successfully paid loans": 65,
        "Outstanding loans": 15.7,
        "Forgiven loans": 5.6,
        "In progress": 2.1,
        "Forfeit": 1.9,
        "Other": 1.5
    }


def loan_balance():
    return {
        "credit_score": 700, 
        "score_increase": 25, 
        "remaining_debt": 15000, 
        "original_loan": 20000, 
    }

def contigency_table(index: pd.Series, column: pd.Series, normalize: Union[bool, str]=False):
    return pd.crosstab(index=index, columns=column, normalize=normalize).round(3)

def plot_stat_one(df: pd.DataFrame, x: str, is_num: bool=False) -> Figure:
    return create_histogram(df, x, is_num)

def plot_stat_two(df: pd.DataFrame, y: str, normalize: Union[bool, str]=False) -> Figure:
    c_table = contigency_table(df[CategoricalFeature.LOAN_STATUS.name.lower()], df[y], normalize)
    return create_heatmap(c_table)

def plot_stat_three(df: pd.DataFrame, y: str) -> Figure:
    return create_boxplot(df, y)

def get_prediction_model(model_name: str):
    models = {
        PredictionModel.RANDOM_FOREST.value: RandomForest,
    }
    class_instance = models.get(model_name, RandomForest)
    return class_instance()

def map_form_to_one_hot_encoding(inputs: list, form_features: List[Enum]) -> Dict:
    encoded_input = {}
    for i in range(len(inputs)):
        encoded_feature_input = map_feature_to_one_hot_encoding(inputs[i], form_features[i])
        encoded_input.update(encoded_feature_input)
    return encoded_input

def map_feature_to_one_hot_encoding(input: Union[int, str], feature: Enum) -> list:
    if isinstance(feature, NumericalFeature):
        return {feature.name: input}

    category = {
        CategoricalFeature.PURPOSE: LoanPurpose,
        CategoricalFeature.TERM: LoanTerm,
    }
    orig_features, _ = feature_list(category.get(feature))
    encoded_feature = dict.fromkeys(orig_features, 0)
    encoded_feature[input] = 1
    return encoded_feature
