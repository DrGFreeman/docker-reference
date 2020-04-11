import dash
import dash_bootstrap_components as dbc

from .layout import layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "Dash app in Docker container"

app.layout = layout

from . import callbacks
