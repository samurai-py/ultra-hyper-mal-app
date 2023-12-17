import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import matplotlib.pyplot as plt

dash.register_page(__name__, path="/animes")

# Adicione uma nova classe CSS para os cards de imagem
card_image_style = {
    "object-fit": "cover",
    "max-height": "100%",
    "max-width": "200%",
    "width": "200%",
    "height": "100%",
}

# Layout da página 'home'
layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='open-new-tab'),
        dbc.Row(
                    [
                        dbc.Col(html.H3("Melhores Classificados"), style={"flex-grow": 9}),
                        dbc.Col(
                            html.Button('Reset', id='reset-val', n_clicks=0),
                            style={"flex-grow": 3},
                        ),
                    ],
                ),
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                # Coluna da esquerda com a imagem
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardImg(
                                            src="URL_DA_IMAGEM",
                                            top=True,
                                            className="card-image",
                                            style={
                                                "height": "300px",
                                                "objectFit": "cover",
                                            },
                                        ),
                                        body=True,
                                    ),
                                    style={"flex-grow": 3},  # Proporção 5
                                ),
                                # Coluna da direita dividida em duas colunas iguais
                                dbc.Col(
                                    [
                                        # Primeira coluna da direita com proporção 4
                                        dbc.Row(
                                            [
                                                dbc.Col(dbc.Card(body=True), style={"flex-grow": 4}),
                                                dbc.Col(dbc.Card(body=True), style={"flex-grow": 8}),
                                            ]
                                        ),
                                        # Segunda coluna da direita com proporção 8
                                        dbc.Row(
                                            [
                                                dbc.Col(dbc.Card(body=True), style={"flex-grow": 8}),
                                                dbc.Col(dbc.Card(body=True), style={"flex-grow": 4}),
                                            ]
                                        ),
                                    ],
                                    style={"flex-grow": 7},  # Proporção 7
                                ),
                            ],
                            style={"display": "flex", "flexWrap": "wrap"},
                        ),
                    ],
                    style={"flex-grow": 1, "display": "flex", "justifyContent": "center"},
                ),
            ],
            style={"display": "flex", "flexWrap": "wrap"},  # Flexbox wrapper styles
        ),
        dbc.Row(
            [
                # Primeira coluna
                dbc.Col(style={"flex-grow": 5}),
                # Segunda coluna dividida em duas rows
                dbc.Col(
                    [
                        # Primeira row
                        dbc.Row(style={"flex-grow": 4}),
                        # Segunda row
                        dbc.Row(style={"flex-grow": 8}),
                    ],
                    style={"flex-grow": 7},
                ),
            ],
            style={"height": "30%"},
            className="flex items-center justify-center w-full",
        ),
        dbc.Row([
            dbc.Card(id='card')
        ], style={"height": "100%"}),
    ],
    style={"height": "100%"},
)
