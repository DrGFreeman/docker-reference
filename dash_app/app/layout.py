import time

import dash_bootstrap_components as dbc
import dash_html_components as html


form = dbc.Form(
    [
        dbc.Input(id="alert_input", placeholder="Input alert text"),
        html.Small("Press a button to display an alert.", className="text-muted"),
        dbc.FormGroup(
            [
                dbc.Button(
                    "Green Alert",
                    id="green_button",
                    color="success",
                    className="mr-2",
                    n_clicks_timestamp=time.time(),
                ),
                dbc.Button(
                    "Red Alert",
                    id="red_button",
                    color="danger",
                    n_clicks_timestamp=time.time(),
                ),
            ]
        ),
    ]
)

body = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H1("Dash app in Docker container"),
                    dbc.Alert(id="alert", is_open=False, dismissable=True),
                    html.H3("Alerts"),
                    form,
                ]
            )
        )
    ],
    className="mt-4",
)

layout = html.Div([body])
