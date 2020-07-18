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

engine = create_engine('postgresql://{0}:{1}@{2}:5432/{3}'.format(user, password, host, database), encoding='utf8')


# -----------------
# Read geoJSON
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, 'data', 'colombiaID.geo.json')
with open(json_path, encoding='utf-8') as json_file:
    departamentos = json.load(json_file)


# -----------------
# Flask app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Saber Pro and TyT"
server = app.server

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
    "mod_competen_ciudada_punt",
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

# Factores
available_factor = [
    'estu_prgm_departamento',
    'estu_metodo_prgm',
    'inst_caracter_academico',
    'inst_origen',
    'estu_nucleo_pregrado',
    'estu_valormatriculauniversidad',
    'estu_genero',
    'estu_horassemanatrabaja',
    'estu_simulacrotipoicfes',
    'fami_estratovivienda'
]

# Género
available_gender = [
    'F',
    'M'
]

# Horas Semana Trabaja
available_work_week_hours = [
    0,
    "Menos de 10 horas",
    "Entre 11 y 20 horas",
    "Entre 21 y 30 horas",
    "Más de 30 horas"
]

# Si No
available_yes_no = [
    'Si',
    'No'
]

# Valor Matrícula Universidad
available_tuition_cost = [
    'No pagó matrícula',
    'Menos de 500 mil',
    'Entre 500 mil y menos de 1 millón',
    'Entre 1 millón y menos de 2.5 millones',
    'Entre 2.5 millones y menos de 4 millones',
    'Entre 4 millones y menos de 5.5 millones',
    'Entre 5.5 millones y menos de 7 millones',
    'Más de 7 millones'
]

# Metodo
available_method = [
    'PRESENCIAL',
    'SEMI-PRESENCIAL',
    'DISTANCIA',
    'DISTANCIA VIRTUAL' 
]

# Tipo Institución
available_inst_type = [
    'NO OFICIAL - CORPORACIÓN',
    'NO OFICIAL - FUNDACIÓN',
    'OFICIAL NACIONAL',
    'OFICIAL DEPARTAMENTAL',
    'OFICIAL MUNICIPAL',
    'REGIMEN ESPECIAL'
]

# Caracter Institución
available_inst_level = [
    'UNIVERSIDAD',
    'INSTITUCIÓN UNIVERSITARIA',
    'INSTITUCIÓN TECNOLÓGICA',
    'TÉCNICA PROFESIONAL',
    'ESCUELA NORMAL SUPERIOR'
]

# Departamento
available_dpto = [
    "AMAZONAS",
    "ANTIOQUIA",
    "ARAUCA",
    "ATLANTICO",
    "BOGOTA",
    "BOLIVAR",
    "BOYACA",
    "CALDAS",
    "CAQUETA",
    "CASANARE",
    "CAUCA",
    "CESAR",
    "CHOCO",
    "CORDOBA",
    "CUNDINAMARCA",
    "GUAINIA",
    "GUAVIARE",
    "HUILA",
    "LA GUAJIRA",
    "MAGDALENA",
    "META",
    "NARIÑO",
    "NORTE SANTANDER",
    "PUTUMAYO",
    "QUINDIO",
    "RISARALDA",
    "SAN ANDRES",
    "SANTANDER",
    "SUCRE",
    "TOLIMA",
    "VALLE",
    "VAUPES",
    "VICHADA"
]


# Presentation Order
presentation_order = {
    'estu_horassemanatrabaja': available_work_week_hours,
    'estu_genero': available_gender,
    'fami_estratovivienda': available_estrato,
    'estu_simulacrotipoicfes': available_yes_no,
    'estu_metodo_prgm': available_method,
    'inst_origen': available_inst_type,
    'inst_caracter_academico': available_inst_level,
    'estu_valormatriculauniversidad': available_tuition_cost
    #'estu_nucleo_pregrado': [],
}


# -----------------
# Name Mappings

presentation_column_names = {
    'estu_nucleo_pregrado': 'Programa: Núcleo de conocimiento',
    'estu_prgm_departamento': 'Institución: Departamento geográfico',
    'estu_genero': 'Personal: Género',
    'fami_estratovivienda': 'Socioeconómico: Estrato',
    'inst_caracter_academico': 'Institución: Nivel',
    'estu_metodo_prgm': 'Institución: Metodología',
    'inst_origen': 'Institución: Régimen',
    'estu_valormatriculauniversidad': 'Programa: Valor Matrícula',
    'estu_simulacrotipoicfes': 'Personal: Preparación de prueba con simulacro',
    'estu_horassemanatrabaja': 'Personal: Horas que trabaja por semana'
}

presentation_column_short_names = {
    'estu_nucleo_pregrado': 'Núcleo de conocimiento',
    'estu_prgm_departamento': 'Departamento geográfico',
    'estu_genero': 'Género',
    'fami_estratovivienda': 'Estrato',
    'inst_caracter_academico': 'Nivel',
    'estu_metodo_prgm': 'Metodología',
    'inst_origen': 'Régimen',
    'estu_valormatriculauniversidad': 'Valor Matrícula',
    'estu_simulacrotipoicfes': 'Preparación de prueba con simulacro',
    'estu_horassemanatrabaja': 'Horas que trabaja por semana'
}

presentation_test = {
    "SaberPro": "Saber Pro",
    "SaberTyT": "Saber TyT"
}

presentation_module = {
    "mod_comuni_escrita_punt": "Comunicación Escrita",
    "mod_competen_ciudada_punt": "Competencias Ciudadanas",
    "mod_lectura_critica_punt": "Lectura Crítica",
    "mod_razona_cuantitat_punt": "Razonamiento Cuantitativo",
    "mod_ingles_punt": "Inglés"
}

# -----------------
# Tabs Styles

tabs_styles = {
    'height': '32px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px 0px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#5DADEC',
    'color': 'white',
    'padding': '6px'
}

# -----------------
# Layout
app.layout = html.Div([
    
    
    # Title
    html.H1("What factors drive Saber Pro and Saber TyT Test results?", style={'text-align':'center'}, id='Title'),

    # Subtitle
    # html.H4("Saber Pro and Saber TyT", style={'text-align':'center'}, id='Subtitle'),

    # Tabs
    dcc.Tabs([
        dcc.Tab(label=' Project Overview', children=[
            
        ],
        style=tab_style,
        selected_style=tab_selected_style
        ),

        dcc.Tab(label='Explore results', children=[
            
            # Row with filter and map
            html.Div([
                # Filter box
                html.Div([

                    html.Div([
                        html.Label('Test'),
                        dcc.Dropdown(
                            id='test-dropdown',
                            options=[{'label': presentation_test[i], 'value': i} for i in available_test],
                            value=available_test[1]
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Module'),
                        dcc.Dropdown(
                            id='module-dropdown',
                            options=[{'label': presentation_module[i], 'value': i} for i in available_module],
                            value=available_module[0]
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Factor'),
                        dcc.Dropdown(
                            id='factor-dropdown',
                            options=[{'label': presentation_column_names[i], 'value': i} for i in available_factor],
                            value="estu_prgm_departamento"
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Year'),
                        html.Br(),
                        dcc.Slider(
                            id='year-slider',
                            min=2016,
                            max=2019,
                            value=2016,
                            marks={str(year): str(year) for year in available_year},
                            step=None
                        )
                    ],
                    className="mini_filter")

                ],
                className="pretty_container four columns",
                id="cross-filter-options"
                ),

                # Graphs
                html.Div([

                    html.Div([
                        dcc.Graph(id='graph-with-filter')
                    ],
                    className="pretty_container"),

                ],
                id="factor-graph-container",
                className="eight columns right-column"
                )
            
            ],
            className="row flex-display multi_filter"
            ),

            # # Row for another graph
            # html.Div([
            #     #
            #     html.Div([
            #         dcc.Graph(id='another-graph')
            #     ])
            # ],
            # className="pretty_container"),

        ],
        style=tab_style,
        selected_style=tab_selected_style
        ),

        dcc.Tab(label='Predict your results', children=[

            # Row with form and predicition
            html.Div([
                # Form box
                html.Div([

                        html.Div([

                            html.Div([
                            html.Label('Test'),
                            dcc.Dropdown(
                                id='test-dropdown-form',
                                options=[{'label': presentation_test[i], 'value': i} for i in available_test],
                                value=None
                            )
                        ],
                        className="mini_filter right-column auto_width flex-1"),

                        html.Div([
                            html.Label('Departament'),
                            dcc.Dropdown(
                                id='departament-dropdown-form',
                                options=[{'label': i.title(), 'value': i} for i in available_dpto],
                                value=None
                            )
                        ],
                        className="mini_filter right-column auto_width flex-1")
                    
                    ],
                    className="row flex-display"
                    ),

                    html.Div([

                        html.Div([
                            html.Label('Gender'),
                            dcc.Dropdown(
                                id='gender-dropdown-form',
                                options=[{'label': i.title(), 'value': i} for i in available_gender],
                                value=None
                            ),
                        ],
                        className="mini_filter right-column auto_width flex-1"),

                        html.Div([
                            html.Label('Stratum'),
                            dcc.Dropdown(
                                id='stratum-dropdown-form',
                                options=[{'label': i.title(), 'value': i} for i in available_estrato],
                                value=None
                            )
                        ],
                        className="mini_filter right-column auto_width flex-1")
                    
                    ],
                    className="row flex-display"
                    ),

                    html.Div([
                        html.Label('Institution Type'),
                        dcc.Dropdown(
                            id='inst-type-dropdown-form',
                            options=[{'label': i.title(), 'value': i} for i in available_inst_type],
                            value=None
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Institution Level'),
                        dcc.Dropdown(
                            id='inst-level-dropdown-form',
                            options=[{'label': i.title(), 'value': i} for i in available_inst_level],
                            value=None
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Tuition cost'),
                        dcc.Dropdown(
                            id='inst-tuition-dropdown-form',
                            options=[{'label': i, 'value': i} for i in available_tuition_cost],
                            value=None
                        )
                    ],
                    className="mini_filter"),

                    html.Div([
                        html.Label('Education Method'),
                        dcc.Dropdown(
                            id='inst-method-dropdown-form',
                            options=[{'label': i.title(), 'value': i} for i in available_method],
                            value=None
                        )
                    ],
                    className="mini_filter")

                ],
                className="pretty_container four columns",
                id="factors-form"
                ),

                # Graphs
                html.Div([

                    html.Div([
                        dcc.Graph(id='graph-with-prediction')
                    ],
                    className="pretty_container"),

                ],
                id="prediction-container",
                className="eight columns right-column"
                )
            
            ],
            className="row flex-display"
            ),

            # # Row for another graph
            # html.Div([
            #     #
            #     html.Div([
            #         dcc.Graph(id='another-graph')
            #     ])
            # ],
            # className="pretty_container"),

        ],
        style=tab_style,
        selected_style=tab_selected_style
        ),

        dcc.Tab(label='About Team 18', children=[],
        style=tab_style,
        selected_style=tab_selected_style
        )
    ],
    style=tabs_styles
    ),
    
])


# -----------------
# Graph Functions

def get_box_plot(selected_test,selected_year, selected_mod, selected_factor):
    query = '''
        SELECT {3}, {0} 
        FROM datafinaldepurado 
        WHERE prueba = '{1}' 
        AND year = {2}
    '''.format(selected_mod, selected_test, selected_year, selected_factor)

    filtered_df = pd.read_sql_query(query,con=engine)
    filtered_df.dropna(inplace=True)

    fig = px.box(filtered_df, x=selected_factor, y=selected_mod, color=selected_factor,
                 category_orders=presentation_order)
    
    fig.update_layout(
        transition_duration=2,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.4,
            xanchor="center",
            x=0.5,
            title=""
        )
    )

    fig.update_xaxes(showticklabels=False, title=presentation_column_short_names[selected_factor])
    fig.update_yaxes(title=presentation_module[selected_mod]) 

    return fig


def get_map(selected_test,selected_year, selected_mod):
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
                               zoom=4, labels=dict(presentation_module, **presentation_column_short_names))

    fig.update_layout(title="Colombia",margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#F8F9F9", plot_bgcolor="#F8F9F9")
    return fig


# -----------------
# Callbacks

# Box Plot Callback
@app.callback(
    Output('graph-with-filter', 'figure'),
    [Input('test-dropdown', 'value'),
    Input('year-slider', 'value'),
    Input('module-dropdown', 'value'),
    Input('factor-dropdown', 'value')])
def update_figure(selected_test,selected_year, selected_mod, selected_factor):
    if selected_factor ==  'estu_prgm_departamento':
        return get_map(selected_test,selected_year, selected_mod)
    elif selected_factor in  ['fami_estratovivienda', 'estu_genero']:
        return get_box_plot(selected_test,selected_year, selected_mod, selected_factor)
    else:
        return get_box_plot(selected_test,selected_year, selected_mod, selected_factor)
    # if selected_factor ==  'estu_nucleo_pregrado':
    # elif selected_factor ==  'inst_caracter_academico':
    # elif selected_factor ==  'estu_metodo_prgm':
    # elif selected_factor ==  'inst_origen':
    # elif selected_factor ==  'estu_valormatriculauniversidad':
    # elif selected_factor ==  'estu_simulacrotipoicfes':
    # elif selected_factor ==  'estu_horassemanatrabaja':


# Radar Chart Callback
@app.callback(
    Output('graph-with-prediction', 'figure'),
    [Input('test-dropdown-form', 'value'),
    Input('departament-dropdown-form', 'value')])
def update_figure(selected_test, selected_dpto):
    df = pd.DataFrame(dict(
        punt=[150, 150, 150, 150, 180],
        module=available_module))
    
    df['module_name'] = df['module'].map(presentation_module)

    fig = px.line_polar(df, r='punt', theta='module_name', line_close=True,
                        labels={'punt': 'Score', 'module_name': 'Module'})

    fig.update_layout(
        polar = dict(
            radialaxis = dict(
                range=[0, 300], 
                showticklabels=True,
                dtick=75
            )
        )
    )
    
    return fig


print('Loading app...')
if __name__ == '__main__':
    app.run_server(debug=True)