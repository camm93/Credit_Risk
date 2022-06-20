import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app.functions import get_user_stats, loan_balance, plot_regression

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Credit Risk Estimator"


server = app.server


def dashboard_menu():
    """
    :return: Div containing dashboard Overview, Loans, History & Settings
    """
    return html.Div(
        id="dashboard-menu",
        children=[
            html.H5("Dashboard"),
            dbc.Button("Overview", color="Light", className="menu-btns"),
            dbc.Button("Your Scorecard", color="Light", className="menu-btns"),
            dbc.Button("History - Stats", color="Light", className="menu-btns"),
            dbc.Button("About", color="Light", className="menu-btns"),
        ],
        className="d-grid gap-2",
    )


def info_cards():
    cards = [
        dbc.Card(
            [
                html.H3("Overview")
            ],
            className="upper-cards",
            color="#F44336"
        ),
        dbc.Card(
            [
                html.H3("Loans Given"),
                html.H3("Loans Taken")
            ],
            className="upper-cards",
            color="#2196F3"
        ),
        dbc.Card(
            [
                html.H3("History")
            ],
            className="upper-cards",
            color="#009688"
        ),
    ]
    return dbc.Row(
        id="upper-stats",
        children=[dbc.Col(card) for card in cards]
    )


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


def lower_stats():
    return html.Div(
        id="lower-stats",
        className="lower-stats",
        children=[
            dbc.Row(
                [dbc.Col(
                    [
                    html.H5("Demographic"),
                    html.Hr(),
                    html.P("Income"),
                    html.P("Loans"),
                    html.P("Funded"),
                    ]
                ),
                dbc.Col(
                    [html.H5(""),
                    html.Hr(),
                    html.P("Settlement"),
                    html.P("Term"),
                    html.P("Rate"),]
                ),
                dbc.Col(
                    [html.H5("Target Users"),
                    html.Hr(),
                    html.P("Users"),
                    html.P("Active"),
                    html.P("HeatMap"),]
                )],
            )
        ]
    )


app.layout = html.Div(
    id="app-container",
    style={"background-color": "#f3f4f5"},
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("plotly_logo.png"))],
        ),
        dbc.Row(
            [dbc.Col(
                children=[html.P("Welcome, User", style={"fontSize": 14}), ],
                width=2,
                style={"background-color": "white", "padding": "auto"}
            ),
            dbc.Col(
                html.B("My Dashboard", style={"color": "black", "font-size": 22, "font-family": "Raleway"}),
                width=10
            )]
        ),
        dbc.Row(
            id="row1",
            children=[
                # Left column
                dbc.Col(
                    dashboard_menu(),
                    width=2,
                    style={"background-color": "white"},
                ),
                # Right column
                dbc.Col(
                    [
                    info_cards(),
                    middle_stats(),
                    bar_stats(),
                    stats_table(),
                    html.Hr(),
                    lower_stats()],
                    width=10
                )
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    return plot_regression(std)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
