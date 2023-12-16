import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

dash.register_page(__name__, path="/")

# Defina suas opções de radioitems
radio_options = [
    {"label": "Melhores", "value": "melhores"},
    {"label": "Piores", "value": "piores"},
]

df_animes = pd.read_csv("data/gold/animes_final.csv")

rank = df_animes.sort_values(by="rank", ascending=True)
rank_top_3 = rank[["anime_id", "title", "img_url"]].head(3)

melhores_classificados_data = []
for index, row in rank_top_3.iterrows():
    card_data = {
        "title": row["title"],
        "image": row["img_url"],
        "link": f'/animes/{row["anime_id"]}',
    }
    melhores_classificados_data.append(card_data)

widths = [3, 6, 3]
for i in range(len(melhores_classificados_data)):
    melhores_classificados_data[i]["width"] = widths[i]

popularity = df_animes.sort_values(by="popularity", ascending=True)
popularity_top_5 = popularity[["anime_id", "title", "img_url"]].head(6)

mais_assistidos_data = []
for index, row in popularity_top_5.iterrows():
    card_data = {
        "title": row["title"],
        "image": row["img_url"],
        "link": f'/animes/{row["anime_id"]}',
    }
    mais_assistidos_data.append(card_data)
    

df_animes_wc = df_animes.copy()

def lista_para_strings(lista):
    # Junte os elementos da lista usando espaços e substitua os espaços por hifens
    return ' '.join(lista)

# Aplicar a função à coluna 'anime_genre'
df_animes_wc['anime_genre'] = df_animes_wc['anime_genre'].apply(eval)  # Converte a string para uma lista de fato
df_animes_wc['anime_genre'] = df_animes_wc['anime_genre'].apply(lista_para_strings)

text = " ".join(genre for genre in df_animes_wc.anime_genre)
    
# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=20,
                    background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('assets/wc.png', bbox_inches='tight')


# Users
df_users = pd.read_csv("data/gold/users_final.csv")
top_users = df_users.sort_values(by='num_reviews', ascending=False)

top_users_data = []
for index, row in top_users.iterrows():
    card_data = {
        "Usuário": row["user_name"],
        "Qtd. Reviews": row["num_reviews"],
    }
    top_users_data.append(card_data)


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
    [   dcc.Location(id='url', refresh=False),
        html.Div(id='open-new-tab'),
        dbc.Row(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H3("Melhores Classificados"), width=9),
                        dbc.Col(
                            dbc.RadioItems(
                                options=radio_options,
                                value=1,
                                id="radioitems-input",
                                inline=True,
                            ),
                            width=3,
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        html.A(
                                            [
                                                dbc.CardImg(
                                                    src=card["image"],
                                                    top=True,
                                                    className="card-image",
                                                    style={
                                                        "height": "300px",
                                                        "objectFit": "cover",
                                                    },  # Fixed height for the image
                                                ),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            card["title"],
                                                            className="card-title",
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            style={
                                                "height": "100%"
                                            },href=card["link"]  # Set the height to 100%
                                        ),
                                    ),
                                    width=card["width"],  # Assign individual widths
                                )
                                for card in melhores_classificados_data
                            ]
                        ),
                    ],
                    md=12,
                    style={"flex-grow": 1, "dislay": "flex", "justifyContent": "center"},
                ),
            ],
            style={"display": "flex", "flexWrap": "wrap"},  # Flexbox wrapper styles
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Mais Assistidos"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                html.A(
                                                    [
                                                        dbc.CardImg(
                                                            src=card["image"],
                                                            top=True,
                                                            className="card-image",
                                                        ),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(
                                                                    card["title"],
                                                                    className="card-title",
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    href=card["link"],
                                                )
                                            ]
                                        ),
                                    ],
                                    md=2,
                                )
                                for card in mais_assistidos_data
                            ],
                            className="g-12",
                        ),
                    ],
                    align="center",
                    md=12,
                ),
            ],
            style={"height": "30%"},
            className="flex items-center justify-center w-full",
        ),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Bag of Words"),
                    dbc.CardBody([
                        html.Img(id='wordcloud',src='assets/wc.png', style={'width': '100%'})
                    ])
                ])
            ], md=6, style={"flex-grow": 1}),
            dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dash_table.DataTable(
                        id='table',
                        columns=[
                            {'name': 'Usuário', 'id': 'Usuário'},
                            {'name': 'Qtd. Reviews', 'id': 'Qtd. Reviews'},
                        ],
                        data=top_users_data,
                        page_size=10
                    )
                ])
            ])
        ], md=6, style={"flex-grow": 1}),
        ], style={"height": "100%"}),
    ],
    style={"height": "100%"},
)

@dash.callback(
    Output('open-new-tab', 'children'),
    [Input('table', 'active_cell')]
)
def open_new_tab(active_cell):
    if active_cell and active_cell['column_id'] == 'Usuário':
        username = top_users_data[active_cell['row']]['Usuário']
        return dcc.Location(pathname=f'/users/{username}', id='dummy-location')
    else:
        return dash.no_update