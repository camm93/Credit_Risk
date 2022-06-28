import dash
from dash import html, dcc, callback, Input, Output
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/about")

layout = html.Div(children=[
    html.H1("About Credit Risk."),
    html.Br(),
    html.P("This is a dashboard for the Credit Risk Estimator."),
    html.P("This dashboard is built with Dash and Dash-Labs."),
    html.P("The data is provided by Lending Club. through a Kaggle challenge"),
    html.Br(),
    html.H2("About the team"),
    html.Br(),
    html.P("This dashboard is built by the 67th team in Data Science 4 All Colombia."),
    html.P("The team is composed of:"),
    html.Br(),
    html.H3("Cristian Alexis Murillo Martínez"),
    html.H3("Juan Cadavid Aguirre"),
    html.H3("Steven Rojas Serrano"),
    html.H3("Daniel Garzón Rodríguez"),
    html.H3("Daniel Espinal Mosquera"),

])