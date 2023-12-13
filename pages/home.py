import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import pandas as pd

dash.register_page(__name__, path='/')

# Defina suas opções de radioitems
radio_options = [{'label': 'Melhores', 'value': 'melhores'},
                 {'label': 'Piores', 'value': 'piores'}]

# Defina seus dados para a Dash-table
dash_table_data = [
    {'Usuário': 'Usuário 1', 'Qtd. Reviews': 10},
    {'Usuário': 'Usuário 2', 'Qtd. Reviews': 5},
    # Adicione mais linhas conforme necessário
]

df_animes = pd.read_csv('data/gold/animes_final.csv')

rank = df_animes.sort_values(by='rank', ascending=True)
rank_top_3 = rank[['anime_id','title', 'img_url']].head(3)

melhores_classificados_data = []
for index, row in rank_top_3.iterrows():
    card_data = {
        'title': row['title'],
        'image': row['img_url'],
        'link': f'/animes/{row["anime_id"]}'
    }
    melhores_classificados_data.append(card_data)

popularity = df_animes.sort_values(by='popularity', ascending=True)
popularity_top_5 = popularity[['anime_id','title', 'img_url']].head(5)

mais_assistidos_data = []
for index, row in popularity_top_5.iterrows():
    card_data = {
        'title': row['title'],
        'image': row['img_url'],
        'link': f'/animes/{row["anime_id"]}'
    }
    mais_assistidos_data.append(card_data)

# Adicione uma nova classe CSS para os cards de imagem
card_image_style = {'object-fit': 'cover', 'max-height': '100%', 'max-width': '200%', 'width': '200%', 'height': '100%'}

# Layout da página 'home'
layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id='radio-selector',
                options=radio_options,
                value='melhores',
                inline=True
            )
        ], md=1),
    ], style={"height": "10vh"}),  # Defina a altura desejada aqui

    dbc.Row([
        dbc.Col([
            html.H3("Melhores Classificados"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        html.A([
                            dbc.CardImg(src=card['image'], top=True, className='card-image'),
                            dbc.CardBody([
                                html.H5(card['title'], className='card-title'),
                            ]),
                        ], href=card['link'])
                    ])
                ], md=4) for card in melhores_classificados_data
            ])
        ], md=12, style={"flex-grow": 1}),
    ], style={"height": "30vh"}),

    dbc.Row([
        dbc.Col([
            html.H3("Mais Assistidos"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        html.A([
                            dbc.CardImg(src=card['image'], top=True, className='card-image'),
                            dbc.CardBody([
                                html.H5(card['title'], className='card-title'),
                            ]),
                        ], href=card['link'])
                    ])
                ], md=2) for card in mais_assistidos_data
            ])
        ], md=12, style={"flex-grow": 1}),
    ], style={"height": "30vh"}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Bag of Words"),
                dbc.CardBody([
                    html.Ul([
                        html.Li("Palavra 1"),
                        html.Li("Palavra 2"),
                        html.Li("Palavra 3"),
                        # Adicione mais palavras conforme necessário
                    ])
                ])
            ])
        ], md=6, style={"flex-grow": 1}),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Dash-Table"),
                dbc.CardBody([
                    dash_table.DataTable(
                        id='table',
                        columns=[
                            {'name': col, 'id': col} for col in dash_table_data[0].keys()
                        ],
                        data=dash_table_data,
                        page_size=5
                    )
                ])
            ])
        ], md=6, style={"flex-grow": 1}),
    ], style={"height": "20vh"}),
], style={"height": "100vh"})
