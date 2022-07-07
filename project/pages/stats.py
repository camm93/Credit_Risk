import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
from dash_labs.plugins.pages import register_page

from enums import CategoricalFeature, AllFeature
from services.functions import plot_stat_one, plot_stat_two, plot_stat_three
from services.utils import feature_equivalence, feature_list, read_feather_db


register_page(__name__, path="/stats")

PREDICTED_FEATURE = CategoricalFeature.LOAN_STATUS.name.lower()

#df = read_feather_db()


def get_feature_dropdown():
    return dcc.Dropdown(options=feature_equivalence(AllFeature), value=feature_equivalence(AllFeature)[0]["value"], id="dropdown-feature")


def upper_plot():
    return dbc.Row(
        id="upper-plot",
        children=[
            get_feature_dropdown(),
            dcc.Graph(id="hist-plot"),
            dcc.Graph(id="box-plot"),
        ]
    )


def describe_table(feature_description: dict):
    cat_features, _ = feature_list(CategoricalFeature)
    table_header = [html.Thead(html.Tr([html.Th("Statistic"), html.Th("Value")]))]
    if feature_description.name in cat_features:
        table_rows = [html.Tr([html.Td(k), html.Td(f"{v}")]) for k, v in feature_description.items()]
    else:
        table_rows = [html.Tr([html.Td(k), html.Td(f"{v:>.2f}")]) for k, v in feature_description.items()]
    table_body = [html.Tbody(table_rows)]
    return dbc.Table(children=table_header + table_body, bordered=True, hover=True, className="describe-table")


def feature_table():
    return html.Div(id="feature-description")


layout = html.Div([
        html.H1("Stats Page"),
        upper_plot(),
        html.H3("Summary Statistics"),
        feature_table(),
])

#@callback(
#    Output(component_id="hist-plot", component_property="figure"),
#    Input(component_id="dropdown-feature", component_property="value")
#)
def update_plot(x: str):
    cat_features, _ = feature_list(CategoricalFeature)
    if x in cat_features:
        return plot_stat_one(df[[x, PREDICTED_FEATURE]], x=x, is_num=False)
    return plot_stat_one(df[[x, PREDICTED_FEATURE]], x=x, is_num=True)

#@callback(
#    Output(component_id="box-plot", component_property="figure"),
#    Input(component_id="dropdown-feature", component_property="value")
#)
def update_plot(y: str):
    cat_features, _ = feature_list(CategoricalFeature)
    if y in cat_features:
        return plot_stat_two(df[[y, PREDICTED_FEATURE]], y=y, normalize="columns")
    else:
        return plot_stat_three(df[[y, PREDICTED_FEATURE]], y=y)

@callback(
    Output(component_id="feature-description", component_property="children"),
    Input(component_id="dropdown-feature", component_property="value")
)
def update_feature_description(x: str):
    return describe_table(df[x].describe())
