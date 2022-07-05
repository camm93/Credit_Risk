from enum import Enum
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

from enums import CategoricalFeature, NumericalFeature
from models.enums import LoanPurpose, LoanTerm, PredictionModel
from services.functions import get_prediction_model, map_form_to_one_hot_encoding
from services.utils import feature_equivalence, model_list


register_page(__name__, path='/scorecard')

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

predictive_model = get_prediction_model(PredictionModel.RANDOM_FOREST.value)

def get_model_dropdown():
    return dcc.Dropdown(
        options=model_list(),
        id='dropdown-model',
        placeholder="Select a predictive model",
        value=model_list()[0],
    )

def predictive_models():
    return html.Div(
        id='model-div',
        children=[
            get_model_dropdown(),
        ],
    )

form_features = [
    NumericalFeature.INT_RATE,
    NumericalFeature.ANNUAL_INC,
    NumericalFeature.LOAN_AMNT,
    NumericalFeature.DTI,
    NumericalFeature.TOTAL_ACC,
    NumericalFeature.INQ_LAST_6MTHS,
    CategoricalFeature.PURPOSE,
    CategoricalFeature.TERM,
]

def return_dcc_type(feature: Enum, i: int, type: str="number"):
    if isinstance(feature, NumericalFeature):
        return dcc.Input(id="input" + str(i), type=type, min=0),
    category = {
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


layout = html.Div([
    html.H1('Score Page'),
    predictive_models(),
    html.Br(),
    inputs,
    html.Br(),
    dbc.Button("Submit", id="submit_btn", color="primary", className="d-grid gap-2 col-2 mx-auto"),
    html.Br(),
    dbc.Button(id="output-predicion", color="success", className="d-grid gap-4 col-4 mx-auto", disabled=True),
    html.Br(),
    dbc.Button(id="output-status", color="success", className="d-grid gap-4 col-4 mx-auto", disabled=True),
])


@callback(
    [Output("output-predicion", "children"),
    Output("output-status", "children"),],
    [State("input" + str(i), "value") for i in range(1, len(form_features) + 1)],
    [State("dropdown-model", "data"),
    Input("submit_btn", "n_clicks")]
)
def update_output(*inputs):
    encoded_input = map_form_to_one_hot_encoding(inputs[:-2], form_features)
    if None in encoded_input:
        return "All fields are mandatory. Please, fill in the form!", "Incomplete Form"

    print(list(encoded_input.values()))
    score, status = predictive_model.predict(list(encoded_input.values())) 
    return score, status
