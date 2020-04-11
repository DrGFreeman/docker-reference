from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from . import app


@app.callback(
    [Output("alert", "children"), Output("alert", "color"), Output("alert", "is_open")],
    [
        Input("green_button", "n_clicks_timestamp"),
        Input("red_button", "n_clicks_timestamp"),
    ],
    [State("alert_input", "value")],
)
def show_alert(green, red, text):
    if green is not None and red is not None:
        if text is None or text == "":
            return "Please enter an alert text in the input field", "warning", True
        if green > red:
            return text, "success", True
        else:
            return text, "danger", True
    else:
        raise PreventUpdate
