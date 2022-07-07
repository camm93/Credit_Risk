import dash_bootstrap_components as dbc
from dash import html
from dash_labs.plugins.pages import register_page
from services.functions import get_user_stats, loan_balance


register_page(__name__, path="/", title="Credit-Risk")


def stats_table():
    more_data_btn = html.Div([dbc.Button("More data", id="more_data_btn", color="danger", href="https://fundpro.com/wdpr/wp-content/uploads/2022/06/comsectorfinanciero032022.pdf" )])
    columns = ['variable',"numero"]
    table_rows = [html.Tr([html.Td(k), html.Td(f"{v:>.2f}")]) for k, v in get_user_stats().items()]
    table_body = [html.Tbody(table_rows)]

    return html.Div(
            [html.H5(" "),
            dbc.Table(table_body, bordered=True, hover=True),
            more_data_btn]
            )

def bar_stats():
    credit_score, score_increase, remaining_debt, original_loan = loan_balance().values()
    return html.Div(
        [
        html.H1("Credit in Colombia. Year 2022", style={'textAlign': 'center'}), 
        #html.P(f"{credit_score} Credit Score"),
        #dbc.Progress(label=f"+{score_increase}%", style={"height": "40px"}, value=score_increase, color="success"),
        html.P(" "),
        dbc.Progress(label=f"Credit statistics in Colombia", style={"height": "40px"}, value=(int(100)), color="success"),
        ],
    )


layout = html.Div([
    bar_stats(),
    stats_table(),
])
