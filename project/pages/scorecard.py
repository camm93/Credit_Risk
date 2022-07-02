import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page
import dash_bootstrap_components as dbc
from numpy import number

register_page(__name__, path='/scorecard')

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

"""
def input_form():
        return dbc.Form(children=[       dbc.Label("Loan Amount"),
                                dbc.Input(type="number", id="loan_amount", value=100000),
                                dbc.Label("Loan Duration"),
                                dbc.Input(type="number", id="loan_duration", value=30),
                                dbc.Label("Interest Rate"),
                                dbc.Input(type="number", id="interest_rate", value=5),
                                dbc.Label("Loan Purpose"),
                                dbc.Input(type="text", id="loan_purpose", value="Home Improvement"),
                                dbc.Label("Loan Type"),
                                dbc.Input(type="text", id="loan_type", value="Conventional"),
                                dbc.Button("Submit", id="submit_btn", color="primary"),

])"""


inputs =dbc.Form(children=[
        dbc.Label("Fico Score "),
        dcc.Input(id="last_fico", type="text", placeholder="Input your Fico score"),
        html.Br(),
        dbc.Label("Interest rate "),
        dcc.Input(id="int_rate", type="text", placeholder="Input your interest rate"),
        html.Br(),
        dbc.Label("Annual income "),
        dcc.Input(id="annual_inc", type="text", placeholder="Input your annual income"),
        html.Br(),
        dbc.Label("Loan amount "),
        dcc.Input(id="loan_amnt", type="text", placeholder="Input your loan ammount"),
        html.Br(),
        html.Div(id="out_table"),  dbc.Button("Submit", id="submit_btn", color="primary"),])
"""    dbc.Label("dti"),
        dcc.Input(id="input5", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("mo_sin_old_rev_tl_op"),
        dcc.Input(id="input6", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("revol_util"),
        dcc.Input(id="input7", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("tot_cur_bal"),
        dcc.Input(id="input8", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("tot_hi_cred_lim"),
        dcc.Input(id="input9", type="text", placeholder="Place your input"),
        html.Br(),
        
        data_table = html.Div(children=[
        clean_data = html.Div([dbc.Button("Clear information", id="clean_data", color="secondary")])
        table_rows = [html.Tr([html.Td(k), html.Td(v)]) for k, v in out_table.items()]
        table_body = [html.Tbody(table_rows)]
        return html.Div(
                [html.H5("Data"),
                dbc.Table(table_body, bordered=True, hover=True),
                clean_data]
        )],id="out_table"))"""
query="Yes"
out_table={}
data_table = html.Div(children=[
        html.Thead(children=[html.Tr([html.Th("Variable "), html.Th("Values")])]),
        html.Tbody(children=[html.Tr([html.Td(k), html.Td(v)]) for k, v in out_table.items()]),
        html.Div(id="out_table")


        ])


layout = html.Div([
        inputs,
        data_table,
       
])

@callback(
    Output("out_table", "children"),
    Input("last_fico", "value"),
    Input("int_rate", "value"),
    Input("annual_inc", "value"),
    Input("loan_amnt", "value"),
    #Input("input6", "value"),
    #Input("input7", "value"),
    #Input("input8", "value"),
    #Input("input9", "value"),
)

def update_output(last_fico, int_rate, annual_inc, loan_amnt):
    return html.Div(u'Fico score {} Interest rate {} Annual income {} Loan ammount {} Is the user expected to pay on time? {}'.format(last_fico, int_rate, annual_inc, loan_amnt, query))

