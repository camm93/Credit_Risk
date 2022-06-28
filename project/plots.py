import pandas as pd
import plotly.express as px

from enums import CategoricalFeature


def create_boxplot(df: pd.DataFrame, y: str=None, color: str=CategoricalFeature.LOAN_STATUS.name.lower()):
    fig = px.box(df, x=color, y=y, color=color,
                 labels={
                           CategoricalFeature.LOAN_STATUS.name.lower(): 'Loan Status'
                        })
    return fig

def create_heatmap(data: pd.DataFrame):
    fig = px.imshow(data, text_auto=True,
                    labels={
                        CategoricalFeature.LOAN_STATUS.name.lower(): 'Loan Status'
                    })
    return fig

def create_histogram(df: pd.DataFrame, x: str, is_num: bool):
    range_x = list(df[x].quantile([0.01, 0.99]).values) if is_num else None
    fig = px.histogram(df, x=x, color=CategoricalFeature.LOAN_STATUS.name.lower(), range_x=range_x,
                       labels={
                           CategoricalFeature.LOAN_STATUS.name.lower(): 'Loan Status'
                        })
    return fig
