import dash
from dash import html, dcc, callback, Input, Output
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/about")

layout = html.Div(children=[
    html.P("About page")
])