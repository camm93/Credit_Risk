import dash_bootstrap_components as dbc
from dash import html
from dash_labs.plugins.pages import register_page
from services.functions import colombia_stats


register_page(__name__, path="/", title="Credit-Risk")


def set_intro():
    return html.Div(
        [
            html.P("In an increasingly connected society, it becomes essential for citizens to be able " +
                   "to access sources of funding, systems of banking, and the option of acquiring credits."),
            html.P("Access to a banking system can create opportunities, create jobs, facilitate commerce, " +
                   "and unlock wealth, nonetheless, only 87% of Colombian adults are registered in " +
                   "the banking system, leaving over five million Colombians without these benefits. " +
                   "The following table summarizes some statistics of the Colombian Financial System.")
        ],
        id="intro-div",
    )


def stats_table():
    more_data_btn = html.Div([dbc.Button(
        "Go to source", id="more_data_btn", color="primary",
        href="https://fundpro.com/wdpr/wp-content/uploads/2022/06/comsectorfinanciero032022.pdf",
        className="d-grid gap-2 col-2 mx-auto")])
    table_header = [html.Thead(
        html.Tr([html.Th("Statistic"), html.Th("Value")]))]
    table_rows = [html.Tr([html.Td(k, className="statistic-table-col"),
                           html.Td(f"{v:>s}", className="value-table-col")]) for k, v in colombia_stats().items()]
    table_body = [html.Tbody(table_rows)]

    return html.Div(
        [html.H5(" "),
         dbc.Table(table_header + table_body, bordered=True,
                   hover=True, className="describe-table"),
         more_data_btn]
    )


layout = html.Div([
    html.H1("State of Credit in Colombia 2022", style={'textAlign': 'center'}),
    set_intro(),
    html.Div(
        id="colombian-financial-system",
        children=html.H6("Colombia's Financial System (* values in Millions of Pesos)")),
    stats_table(),
])
