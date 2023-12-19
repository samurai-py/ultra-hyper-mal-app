import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dash.register_page(__name__, path="/animes")

df_animes = pd.read_csv("data/gold/animes_final.csv")
df_distribution = pd.read_csv("data/gold/users_distribuition_final.csv")

df_animes_fm = df_animes.loc[df_animes["anime_id"] == 5114]

image = df_animes_fm["img_url"].values[0]
episodes = df_animes_fm["episodes"].values[0]
genre = df_animes_fm["anime_genre"].values[0]
genre_list = eval(genre)

# Gráfico Gênero

df_distribution.fillna('Others', inplace=True)
# Filtrar df_distribution pelo anime_id 1
df_distribution_filtered = df_distribution[df_distribution['anime_id'] == 5114]

# Contar a distribuição de gêneros
genre_counts = df_distribution_filtered['user_gender'].value_counts().reset_index()

# Renomear as colunas
genre_counts.columns = ['user_gender', 'count']

# Mapear as cores
colors = {'Male': '#0CB1F7', 'Female': '#F053A7', 'Others': '#A7A7A7'}
genre_counts['color'] = genre_counts['user_gender'].map(colors)

# Criar o gráfico de rosca
fig = px.pie(
    genre_counts,
    values='count',
    names='user_gender',
    color='user_gender',
    color_discrete_map=colors,
    title='Distribuição de Gêneros para anime_id 1'
)

# Adicionar um círculo no meio para criar um efeito de donut
fig.update_layout(
    showlegend=False,
    annotations=[dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

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
                                            src=image,
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
                                                dbc.Col(dbc.Card(
                                                    [
                                                        html.H3(episodes, id='anime-episodes'),
                                                        html.H5('Episódios', id='anime-episodes-label')
                                                    ]
                                                        ,body=True), style={"flex-grow": 4}),
                                                dbc.Col(dbc.Card(
                                                [
                                                      # Use a função eval para avaliar a string como uma lista

                                                    # Iterar sobre a lista de gêneros para criar caixas coloridas
                                                    html.Div([
                                                        html.Div(g, className='genre-box', style={'backgroundColor': 'lightblue'})
                                                        for g in genre_list
                                                    ], className='genre-container'),
                                                    html.H5('Categorias', id='anime-genre-label')
                                                ]
                                                ,body=True), style={"flex-grow": 4}
                                            ),
                                        ]),
                                        # Segunda coluna da direita com proporção 8
                                        dbc.Row(
                                            [
                                                dbc.Col(dbc.Card([dcc.Graph(figure=fig, id='gender_chart')], body=True), style={"flex-grow": 8}),
                                                dbc.Col(dbc.Card(body=True), style={"flex-grow": 8}),
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
