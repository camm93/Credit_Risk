import dash
from enum import Enum
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from numpy import place
from enums import AllFeature, CategoricalFeature, NumericalFeature
from models.enums import LoanGrade, LoanPurpose, LoanTerm
from services.functions import get_prediction_model
from services.utils import feature_equivalence, model_list


register_page(__name__, path='/scorecard')

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

def get_model_dropdown():
    return dcc.Dropdown(
        options=model_list(),
        id='dropdown-model',
        placeholder="Select a predictive model"
    )

def prediction_result():
    return html.Div(
        id='model-div',
        children=[
            get_model_dropdown(),
            html.P(id='predictive-model'),
        ]
    )

form_features = [
    CategoricalFeature.GRADE,
    CategoricalFeature.PURPOSE,
    CategoricalFeature.TERM,
    NumericalFeature.ANNUAL_INC,
    NumericalFeature.DTI,
    NumericalFeature.INQ_LAST_6MTHS,
    NumericalFeature.INT_RATE,
    NumericalFeature.LOAN_AMNT,
]

def return_dcc_type(feature: Enum, i: int, type: str="number"):
    if isinstance(feature, NumericalFeature):
        return dcc.Input(id="input" + str(i), type=type),
    category = {
        CategoricalFeature.GRADE: LoanGrade,
        CategoricalFeature.PURPOSE: LoanPurpose,
        CategoricalFeature.TERM: LoanTerm,
    }
    return dcc.Dropdown(id="input" + str(i), options=feature_equivalence(category.get(feature))),

inputs = dbc.Form(
    children=[
        dbc.Row([
            dbc.Col(dbc.Label(feature.value)),
            dbc.Col(return_dcc_type(feature, i))
            ]) for i, feature in enumerate(form_features, start=1)]
)

out_table={}
data_table = html.Div(children=[
        html.Thead(children=[html.Tr([html.Th("Variable"), html.Th("Value")])]),
        html.Tbody(children=[html.Tr([html.Td(k), html.Td(v)]) for k, v in out_table.items()]),
        html.Div(id="out_table")
])


layout = html.Div([
    html.H1('Score Page'),
    prediction_result(),
    inputs,
    html.Div(id="out_table"),  dbc.Button("Submit", id="submit_btn", color="primary"),
    data_table,
])


@callback(
    Output('predictive-model', 'children'),
    Input('dropdown-model', 'value')
)
def update_result(val: str):
    prediction_model = get_prediction_model(val)
    print(prediction_model)
    return val


@callback(
    Output("out_table", "children"),
    [Input("input" + str(i), "value") for i in range(1, len(form_features) + 1)]
)
def update_output(*inputs):
    # model.predit(inputs)
    print(list(inputs))
    return
