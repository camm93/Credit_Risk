from dash import html
from dash_labs.plugins.pages import register_page


register_page(__name__)

layout = html.Img(src="../assets/not_found.png")