import dash
from dash import dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page
from services.utils import model_list

register_page(__name__, path='/scorecard')

def get_model_dropdown():
    return dcc.Dropdown(options=model_list(), id='dropdown-model')

def prediction_result():
    return html.Div(
        id='model-div',
        children=[
            get_model_dropdown(),
            html.P(id='predictive-model'),
        ]
    )

layout = html.Div([
    html.H1('Score Page'),
    prediction_result(),
])

@callback(
    Output('predictive-model', 'children'),
    Input('dropdown-model', 'value')
)
def update_result(val: str):
    return val
