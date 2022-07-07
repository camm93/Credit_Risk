import pandas as pd
import plotly.express as px

from enums import CategoricalFeature


def create_boxplot(df: pd.DataFrame, y: str=None, color: str=CategoricalFeature.LOAN_STATUS.name.lower()):
    fig = px.box(df, x=color, y=y, color=color,
                 labels={
                           CategoricalFeature.LOAN_STATUS.name.lower(): "Loan Status"
                        })
    return fig

def create_heatmap(data: pd.DataFrame):
    feature = data.columns.name
    fig = px.imshow(data, text_auto=True, title=f"Loan status fraction per {feature}".title(),
                    labels={
                        CategoricalFeature.LOAN_STATUS.name.lower(): "Loan Status"
                    })
    return fig

def create_histogram(df: pd.DataFrame, x: str, is_num: bool):
    fig = px.histogram(df, x=x, color=CategoricalFeature.LOAN_STATUS.name.lower(), #range_x=range_x,
                       labels={
                           CategoricalFeature.LOAN_STATUS.name.lower(): "Loan Status"
                        })
    return fig
