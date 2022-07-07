import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_labs as dl


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], plugins=[dl.plugins.pages])
app.title = "Credit Risk Estimator"


server = app.server

app.config.suppress_callback_exceptions=True


def dashboard_menu():
    """
    :return: Div containing dashboard Overview, Loans, History & Settings
    """
    return html.Div(
        id="dashboard-menu",
        children=[
            html.H5("Dashboard"),
            dbc.Button("Overview", color="Light", className="menu-btns", href="/"),
            dbc.Button("History - Stats", color="Light", className="menu-btns", href="/stats"),
            dbc.Button("Your Scorecard", color="Light", className="menu-btns", href="/scorecard"),
            dbc.Button("About", color="Light", className="menu-btns", href="/about"),
        ],
        className="d-grid gap-2",
    )


app.layout = html.Div(
    id="app-container",
    style={"background-color": "#f3f4f5"},
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(id="logo", src=app.get_asset_url("credit_risk.png"))],
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
                    dl.plugins.page_container,
                    html.Hr(),
                    ],
                    width=10
                )
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
