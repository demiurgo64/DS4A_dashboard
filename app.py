import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import json
import os

from sqlalchemy import create_engine


# -----------------
# DB connection
user = 'postgres'
password = 'postgres'
host = 'localhost'
database = 'icfes'

engine = create_engine('postgresql://{0}:{1}@{2}:5432/{3}'.format(user, password, host, database))


# -----------------
# Read geoJSON
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, 'data', 'colombiaID.geo.json')
with open(json_path) as json_file:
    departamentos = json.load(json_file)


# -----------------
# Flask app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Saber Pro and TyT"


# -----------------
# Constants

# Prueba
available_test = [
    "SaberPro",
    "SaberTyT"
]

# Modulo
available_module = [
    "mod_comuni_escrita_punt",
    "mod_competen_ciudad_punt",
    "mod_lectura_critica_punt",
    "mod_razona_cuantitat_punt",
    "mod_ingles_punt"
]

# Periodo
available_year = [
    2016,
    2017,
    2018,
    2019
]

# Estrato
available_estrato = [
    "Estrato 0",
    "Estrato 1",
    "Estrato 2",
    "Estrato 3",
    "Estrato 4",
    "Estrato 5",
    "Estrato 6",
    "Sin Estrato",
    "Zona Rural"
]

# -----------------
# Layout
app.layout = html.Div([
    
    html.H1("ICFES Test Dashboard", style={'text-align':'center'}, id='Title'),

    html.Div([
        html.Label('Test'),
        dcc.Dropdown(
            id='filter-test',
            options=[{'label': i.upper(), 'value': i} for i in available_test],
            value=available_test[0]
        )
    ]),


    html.Div([
        html.Label('Module'),
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i.upper(), 'value': i} for i in available_module],
            value="mod_comuni_escrita_punt"
        )
    ]),    

    html.Div([
        html.Label('Period'),
        dcc.Slider(
            id='year-slider',
            min=2016,
            max=2019,
            value=2016,
            marks={str(year): str(year) for year in available_year},
            step=None
        )
    ]),

    html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Graph(id='map')
    ]),

    html.Div(
        id = "loading-chart"
    )
])


# -----------------
# Callbacks

# Box Plot Callback
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('filter-test', 'value'),
    Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_figure(selected_test,selected_year, selected_mod):
    query = '''
        SELECT fami_estratovivienda, {0} 
        FROM datafinaldepurado 
        WHERE prueba = '{1}' 
        AND year = {2}
    '''.format(selected_mod, selected_test, selected_year)

    filtered_df = pd.read_sql_query(query,con=engine)
    filtered_df.dropna(inplace=True)

    var_partition = "fami_estratovivienda"
    fig = px.box(filtered_df, x=var_partition, y=selected_mod, color=var_partition,
                 category_orders={"fami_estratovivienda": available_estrato})
    
    fig.update_layout(transition_duration=2)
    fig.update_yaxes(title=selected_mod) 

    return fig


# Map Callback
@app.callback(
    Output('map', 'figure'),
    [Input('filter-test', 'value'),
    Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_map(selected_test,selected_year, selected_mod):
    query = '''
        SELECT *
        FROM fact_estu_prgm_departamento
        WHERE prueba = '{0}'
        AND year = {1}
    '''.format(selected_test,selected_year)

    map_df = pd.read_sql_query(query, con=engine)
    
    fig = px.choropleth_mapbox(map_df, geojson=departamentos, locations='estu_prgm_departamento', 
                               color=selected_mod, color_continuous_scale="Viridis",
                               center={'lat':4.6683288,'lon':-74.1350578}, mapbox_style="carto-positron", 
                               zoom=4)

    fig.update_layout(title="Colombia",margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#F8F9F9", plot_bgcolor="#F8F9F9")
    return fig


print('Loading app...')
if __name__ == '__main__':
    app.run_server(debug=True)