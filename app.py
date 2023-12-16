import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LUMEN])
server = app.server
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#292929",
    "text-color": "#FFFFFF",
}

NAVLINK_STYLE = {
    "color": "#FFFFFF",
    "text-decoration": "none",
}

sidebar = html.Div(
    [
        html.Img(src='/assets/logo.svg', height='150px', className='clickable-logo'),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Animes", href="/animes", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Users", href="/users", active="exact", style=NAVLINK_STYLE),
                dbc.NavLink("Docs", href="/documentation", active="exact", style=NAVLINK_STYLE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Layout do aplicativo
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row([
            dbc.Col([sidebar], width=2, style={"padding": "0px"}),  # Sidebar column
            dbc.Col([dash.page_container], width=10),  # Content column
        ]),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
