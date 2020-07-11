import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import json

df = pd.read_csv('data/data-final-depurado-fecha.csv')
df.fillna(value={'FAMI_ESTRATOVIVIENDA':'-'}, inplace=True)
array=[str(x)[:4] for x in df['PERIODO-X'].values]
df['YEAR']=[int(x) for x in array]

avalaible_test=df.PRUEBA.unique()

avalaible_module=["MOD_COMUNI_ESCRITA_PUNT","MOD_COMPETEN_CIUDADA_PUNT","MOD_LECTURA_CRITICA_PUNT","MOD_RAZONA_CUANTITAT_PUNT","MOD_INGLES_PUNT"]

with open('data/colombiaID.geo.json') as json_file:
    deparments = json.load(json_file)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    html.H1("ICFES Test Dashboard", style={'text-align':'center'}, id='Title'),

    html.Div([
        html.Label('Test'),
        dcc.Dropdown(
            id='filter-test',
            options=[{'label': i, 'value': i} for i in avalaible_test],
            value='SaberPro'
        )
    ]),


    html.Div([
        html.Label('Module'),
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i} for i in avalaible_module],
            value="MOD_COMUNI_ESCRITA_PUNT"
        )
    ]),    

    dcc.Graph(id='graph-with-slider'),
    html.Div([
    dcc.Slider(
        id='year-slider',
        min=df['YEAR'].min(),
        max=df['YEAR'].max(),
        value=df['YEAR'].min(),
        marks={str(year): str(year) for year in df['YEAR'].unique()},
        step=None
    )]),
    html.Div([
    dcc.Graph(id='map')
    ])
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('filter-test', 'value'),
    Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_figure(selected_test,selected_year, selected_mod):
    filtered_df = df[(df['YEAR'] == selected_year) & (df.PRUEBA == selected_test)]
    estratos={'FAMI_ESTRATOVIVIENDA':['Estrato 0', 'Estrato 1', 'Estrato 2', 'Estrato 3', 'Estrato 4', 'Estrato 5','Estrato 6', 'Sin Estrato', 'Zona Rural', '-']}
    fig = px.box(filtered_df, x="FAMI_ESTRATOVIVIENDA", y=selected_mod, color="FAMI_ESTRATOVIVIENDA", category_orders=estratos)

    fig.update_layout(transition_duration=2)

    fig.update_yaxes(title=selected_mod) 

    return fig


@app.callback(
    Output('map', 'figure'),
    [Input('filter-test', 'value'),
    Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_map(selected_test,selected_year, selected_mod):
    filtered_df = df[(df['YEAR'] == selected_year) & (df.PRUEBA == selected_test)]
    df1=filtered_df.groupby('ESTU_PRGM_DEPARTAMENTO').mean().reset_index()
    limite=df1[selected_mod].max()
    fig = px.choropleth_mapbox(df1, geojson=deparments, locations='ESTU_PRGM_DEPARTAMENTO', color=selected_mod, color_continuous_scale="Viridis",
    center={'lat':4.6683288,'lon':-74.1350578}, mapbox_style="carto-positron", zoom=4, range_color=[0, limite])
    fig.update_layout(title="Colombia",margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#F8F9F9", plot_bgcolor="#F8F9F9")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)