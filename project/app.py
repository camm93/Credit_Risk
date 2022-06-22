import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_labs as dl


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], plugins=[dl.plugins.pages])
app.title = "Credit Risk Estimator"


server = app.server


#navbar = dbc.NavbarSimple([
#        dbc.NavItem(dbc.NavLink(page['name'], href=page['path']))
#        for page in dash.page_registry.values()
#        if page["module"] != "pages.not_found_404"
#], brand='Dash App')


def dashboard_menu():
    """
    :return: Div containing dashboard Overview, Loans, History & Settings
    """
    return html.Div(
        id="dashboard-menu",
        children=[
            html.H5("Dashboard"),
            dbc.Button("Overview", color="Light", className="menu-btns", href="/overview"),
            dbc.Button("Your Scorecard", color="Light", className="menu-btns", href="/scorecard"),
            dbc.Button("History - Stats", color="Light", className="menu-btns"),
            dbc.Button("About", color="Light", className="menu-btns", href="/about"),
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
        #navbar,
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
                    dl.plugins.page_container,
                    html.Hr(),
                    lower_stats()],
                    width=10
                )
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
