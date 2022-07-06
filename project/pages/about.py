from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


register_page(__name__, path="/about")

layout = html.Div(children=[
    html.H1("About Credit Risk."),
    html.Br(),
    html.A("GitHub Repository", href="https://github.com/DanielDi/Credit_Risk"),
    html.Br(),
    html.P("This is a dashboard for the Credit Risk Estimator."),
    html.P("This dashboard is built with Dash and Dash-Labs."),
    html.P("The data is provided by Lending Club. through a Kaggle challenge"),
    html.Br(),
    html.H2("About the team"),
    html.Br(),
    html.P(children=["This dashboard is built by the 67th team in Data Science 4 All Colombia.",
    html.A(" Correlation One.", href="https://www.correlation-one.com/data-science-for-all-colombia")]),
    html.P("Team Members:"),
    html.Br(),
    html.Div(
        [

            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    children=[
                                        html.H3("Cristian Alexis Murillo Martínez",
                                                className="card-name"),
                                        html.H5("crismur_93@hotmail.com",
                                                className="card-email"),
                                        html.P("Engineer, Developer and Data Scientist.",
                                               className="card-text"),
                                        dbc.CardLink(
                                            "LinkedIn", href="https://www.linkedin.com/in/cristianmurillom/"),
                                        dbc.CardLink(
                                            "GitHub", href="https://github.com/camm93"),
                                    ],
                                ),
                                dbc.CardFooter(
                                    "(+57)322-305-0192 - Colombia. crismur93@gmail.com")
                            ],
                            color="secondary",
                            outline=True,
                        ),),

                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    children=[
                                        html.H3("Daniel Garzón Rodríguez",
                                                className="card-name"),
                                        html.H5("daalgaro@gmail.com",
                                                className="card-email"),
                                        html.P("Mathematician.",
                                               className="card-text"),
                                        dbc.CardLink(
                                            "LinkedIn", href="https://www.linkedin.com/in/daniel-garz%C3%B3n-rodr%C3%ADguez-540b06145/"),
                                    ],
                                ),
                                dbc.CardFooter(
                                    "(+57)320-248-0219 - Colombia")
                            ],
                            color="secondary",
                            outline=True,),
                        )
                ],
                className="card-row",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    children=[
                                        html.H3("Daniel Espinal Mosquera",
                                                className="card-name"),
                                        html.H5("danieldi0102@gmail.com",
                                                className="card-email"),
                                        html.P("Some text",
                                               className="card-text"),
                                        dbc.CardLink(
                                            "LinkedIn", href="https://www.linkedin.com/in/daniel-espinal/"),
                                        dbc.CardLink(
                                            "GitHub", href="https://github.com/DanielDi"),
                                    ],
                                ),
                                dbc.CardFooter(
                                    "(+57)301-378-7816 - Colombia")
                            ],
                            color="secondary",
                            outline=True,
                        ),),

                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    children=[
                                        html.H3("Juan Pablo Cadavid Aguirre",
                                                className="card-name"),
                                        html.H5("aleg448@gmail.com",
                                                className="card-email"),
                                        html.P("Web 3.0 enthusiast with a love for decentralized solutions.",
                                               className="card-text"),
                                        dbc.CardLink(
                                            "LinkedIn", href="https://www.linkedin.com/in/juan-pablo-cadavid-aguirre/"),
                                        dbc.CardLink(
                                            "GitHub", href="https://github.com/aleg448"),
                                    ],
                                ),
                                dbc.CardFooter(
                                    "(+57)311-741-2549 - Colombia")
                            ],
                            color="secondary",
                            outline=True,),
                        )
                ],
                className="card-row",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    children=[
                                        html.H3("Steven Rojas Serrano",
                                                className="card-name"),
                                        html.H5("stevenrojas354@gmail.com",
                                                className="card-email"),
                                        html.P("Some text",
                                               className="card-text"),
                                        dbc.CardLink(
                                            "LinkedIn", href="https://www.linkedin.com/in/steven-rojas-serrano-99259a206"),
                                    ],
                                ),
                                dbc.CardFooter(
                                    "(+57)315-376-9502 - Colombia")
                            ],
                            color="secondary",
                            outline=True,
                        style={"width": "49.5%"},
                        )
                        ),
                ],
                className="card-row",
            ),
        ]
    )
])
