from this import d
import dash
from dash import dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/scorecard')

def input_form():
        return dbc.Form(
                [
                        dbc.FormGroup(
                                [
                                        dbc.Label("Loan Amount"),
                                        dbc.Input(type="number", id="loan_amount", value=100000),
                                        dbc.Label("Loan Duration"),
                                        dbc.Input(type="number", id="loan_duration", value=30),
                                        dbc.Label("Interest Rate"),
                                        dbc.Input(type="number", id="interest_rate", value=5),
                                        dbc.Label("Loan Purpose"),
                                        dbc.Input(type="text", id="loan_purpose", value="Home Improvement"),
                                        dbc.Label("Loan Type"),
                                        dbc.Input(type="text", id="loan_type", value="Conventional"),
                                ]
                        ),
                        dbc.Button("Submit", id="submit_btn", color="primary"),
                ]
        )

def data_table():
        clean_data = html.Div([dbc.Button("Clear information", id="clean_data", color="secondary")])
        table_rows = [html.Tr([html.Td(k), html.Td(f"{v:>.2f}%")]) for k, v in get_user_stats().items()]
        table_body = [html.Tbody(table_rows)]
        return html.Div(
                [html.H5("Data"),
                dbc.Table(table_body, bordered=True, hover=True),
                clean_data]
        )

layout = html.Div([
        input_form(),
        data_table(),
])
        

                        
