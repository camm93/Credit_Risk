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
        dbc.Label("Fico Score"),
        dcc.Input(id="input1", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("interest rates"),
        dcc.Input(id="input2", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("DTI"),
        dcc.Input(id="input3", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("Installment"),
        dcc.Input(id="input4", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("max_bal_bc"),
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
        dbc.Label("bc_open_to_buy"),
        dcc.Input(id="input10", type="text", placeholder="Place your input"),
        html.Br(),
        dbc.Label("loan_amnt"),
        dcc.Input(id="input11", type="text", placeholder="Place your input"),
        html.Div(id="out_table"),  dbc.Button("Submit", id="submit_btn", color="primary"),]
)

"""data_table = html.Div(children=[
        clean_data = html.Div([dbc.Button("Clear information", id="clean_data", color="secondary")])
        table_rows = [html.Tr([html.Td(k), html.Td(v)]) for k, v in out_table.items()]
        table_body = [html.Tbody(table_rows)]
        return html.Div(
                [html.H5("Data"),
                dbc.Table(table_body, bordered=True, hover=True),
                clean_data]
        )],id="jose")"""
out_table={}
data_table = html.Div(children=[
        html.Thead(children=[html.Tr([html.Th("Variable"), html.Th("Value")])]),
        html.Tbody(children=[html.Tr([html.Td(k), html.Td(v)]) for k, v in out_table.items()]),
        html.Div(id="out_table")


        ])


layout = html.Div([
        inputs,
        data_table,
       
])

@callback(
    Output("out_table", "children"),
    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value"),
    Input("input4", "value"),
    Input("input5", "value"),
    Input("input6", "value"),
    Input("input7", "value"),
    Input("input8", "value"),
    Input("input9", "value"),
    Input("input10", "value"),
    Input("input11", "value"),
)

def update_output(input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11):
    return u'Input 1 {} and Input 2 {} and Input 3 {} and Input 4 {} and Input 5 {} and Input 6 {} and Input 7 {} and Input 8 {} and Input 9 {} and Input 10 {} and Input 11 {}'.format(input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11)

