from enum import Enum
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

from enums import CategoricalFeature, NumericalFeature
from models.enums import LoanPurpose, LoanTerm, PredictionModel
from services.functions import get_prediction_model, map_form_to_one_hot_encoding
from services.utils import calculate_percentile, feature_equivalence, model_list, peso_to_dollar, read_feather_db


register_page(__name__, path="/scorecard")

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

predictive_model = get_prediction_model(PredictionModel.RANDOM_FOREST.value)

last_fico = read_feather_db()['last_fico']

def get_model_dropdown():
    return dcc.Dropdown(
        options=model_list(),
        id="dropdown-model",
        placeholder="Select a predictive model",
        value=model_list()[0],
    )

def predictive_models():
    return html.Div(
        id="model-div",
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

feature_restrictions = [
    (6, 35, 0.1),  # min_, max_, step_
    (0, 1e9, 1e5),
    (0, 1e9, 1e5),
    (0, 40, 0.5),
    (0, 40, 1),
    (0, 5, 1),
    (None, None, None),
    (None, None, None),
]

def return_dcc_type(feature: Enum, i: int):
    if isinstance(feature, NumericalFeature):
        min_, max_, step_ = feature_restrictions[i-1]
        return dcc.Input(id="input" + str(i), min=min_, max=max_, step=step_, type="number", className="input-type", debounce=True),
    category = {
        CategoricalFeature.PURPOSE: LoanPurpose,
        CategoricalFeature.TERM: LoanTerm,
    }
    return dcc.Dropdown(id="input" + str(i), options=feature_equivalence(category.get(feature)), className="dropdown-type"),

inputs = dbc.Form(
    children=[
        dbc.Row([
            dbc.Col(dbc.Label(feature.value)),
            dbc.Col(return_dcc_type(feature, i))
            ]) for i, feature in enumerate(form_features, start=1)]
)


layout = html.Div([
    html.H1("Score Page"),
    predictive_models(),
    html.Br(),
    dcc.ConfirmDialog(
        id="loan-amount-alert",
        message=f"This loan amount exceeds your debt capacity! Replacing entered value with maximum allowed amount.",
    ),
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
    inputs = list(inputs)
    inputs[1] = peso_to_dollar(inputs[1])
    inputs[2] = peso_to_dollar(inputs[2])

    encoded_input = map_form_to_one_hot_encoding(inputs[:-2], form_features)
    if None in encoded_input:
        return "All fields are mandatory. Please, fill in the form!", "Incomplete Form"

    score, status = predictive_model.predict(list(encoded_input.values()))
    percentile_population = (f"Your estimated score is: {score:>.1f}. \n"  
                             f"It is over {calculate_percentile(score, last_fico):>.1f}% of our users.")
    return percentile_population, status

@callback(
    [Output("loan-amount-alert", "displayed"),
     Output("input3", "value")],
    [Input("input2", "value"),
     Input("input3", "value")]
)
def validate_loan_amount(income: int, loan: int):
    print(income, loan)
    if not income or not loan:
        return False, loan
    max_allowed_loan = 1.5 * income
    if loan <= max_allowed_loan:
        return False, loan
    return True, max_allowed_loan
