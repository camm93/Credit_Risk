import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page
from app.functions import get_user_stats, loan_balance, plot_regression


register_page(__name__, path='/overview')


def stats_table():
    more_data_btn = html.Div([dbc.Button("More data >", id="more_data_btn", color="secondary")])
    table_rows = [html.Tr([html.Td(k), html.Td(f"{v:>.2f}%")]) for k, v in get_user_stats().items()]
    table_body = [html.Tbody(table_rows)]

    return html.Div(
            [html.H5("Data"),
            dbc.Table(table_body, bordered=True, hover=True),
            more_data_btn]
            )


def middle_stats():
    return dbc.Row(
        id="middle-stats",
        children=[
            html.Div(
                id="plot_container",
                children=[
                    dcc.Graph(id="regression_plot"),
                    html.P(
                        "Standard Deviation", style={"color": "white", "marginLeft": "20px"}
                    ),
                    dcc.Slider(
                        id="std_slider",
                        min=0,
                        max=40,
                        step=0.5,
                        value=10,
                        marks={i: str(i)
                               for i in range(0, 40, 5)},
                    ),
                ]
            ),
        ]
    )


def bar_stats():
    credit_score, score_increase, remaining_debt, original_loan = loan_balance().values()
    return html.Div(
        [
        html.H5("General Stats"),
        html.P(f"{credit_score} Credit Score"),
        dbc.Progress(label=f"+{score_increase}%", style={"height": "40px"}, value=score_increase, color="success"),
        html.P("Loans available"),
        dbc.Progress(label=f"USD {remaining_debt}/{original_loan}", style={"height": "40px"}, value=(int(remaining_debt/original_loan*100)), color="danger"),
        ],
    )


layout = html.Div([
    middle_stats(),
    bar_stats(),
    stats_table(),
])


@callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    return plot_regression(std)

