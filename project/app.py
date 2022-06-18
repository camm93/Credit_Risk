import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app.functions import plot_regression

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
            html.H4("Dashboard"),
            dbc.Button("Overview", color="Light", style={"text-align": "left"}),
            dbc.Button("Loans", color="Light", style={"text-align": "left"}),
            dbc.Button("History", color="Light", style={"text-align": "left"}),
            dbc.Button("Settings", color="Light", style={"text-align": "left"}),
            html.Div(
                id="intro",
                children="Explore this app 2."
            ),
        ],
        className="d-grid gap-2",
    )

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

def stats_table():
    table_rows = [html.Tr([html.Td("String"), html.Td("Number")]) for i in range(6)]
    table_body = [html.Tbody(table_rows)]
    return dbc.Table(table_body, bordered=True)

more_data_btn = html.Div(
    [
        dbc.Button(
            "More data", id="more_data_btn", color="secondary"
        )
    ]
)

app.layout = html.Div(
    id="app-container",
    style={"margin": "10px"},
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("plotly_logo.png"))],
        ),
        dbc.Row(
            [dbc.Col(
                children=[html.P("Welcome, ", style={"fontSize": 14}), 
                 html.Strong("User", style={"color": "red"})],
                width=2,
                style={"padding": "auto"}
            ),
            dbc.Col(
                html.H4("My Dashboard", style={"color": "blue"}),
                width=10
            )]
        ),
        dbc.Row(
            id="row1",
            children=[
                # Left column
                dbc.Col(
                    dashboard_menu(),
                    # + [
                    #    html.Div(
                    #        ["initial child"], id="output-clientside", style={"display": "none"}
                    #    )
                    # ],
                    width=2,
                ),
                # Right column
                dbc.Col(
                    [
                    dbc.Row(
                        id="upper-stats",
                        children=[dbc.Col(card) for card in cards],
                        style={"margin": "10px"}
                    ),
                    dbc.Row(
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
                    ),
                    html.Div(
                        [html.H5("General Status"),
                        html.P("Credit Score"),
                        html.P("Loans available")]
                    ),
                    html.Div(
                        [html.H5("Data"),
                        stats_table(),
                        more_data_btn]
                    ),
                    html.Hr(),
                    html.Div(
                        id="lower-stats",
                        className="lower-stats",
                        children=[
                            dbc.Row(
                                [dbc.Col(
                                    [
                                    html.H5("Demographic"),
                                    html.P("Income"),
                                    html.P("Loans"),
                                    html.P("Funded"),
                                    ]
                                ),
                                dbc.Col(
                                    [html.H5(""),
                                    html.P("Settlement"),
                                    html.P("Term"),
                                    html.P("Rate"),]
                                ),
                                dbc.Col(
                                    [html.H5("Target Users"),
                                    html.P("Users"),
                                    html.P("Active"),
                                    html.P("HeatMap"),]
                                )],
                            )
                        ]
                    ),
                    ],
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
