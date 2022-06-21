import dash
from dash import dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page

register_page(__name__, path='/scorecard')

layout = html.Div([
        html.H1('Score Page')
])