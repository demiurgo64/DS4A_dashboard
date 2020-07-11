import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

#df = pd.read_csv('db/data-final-depurado.csv',
#    dtype={"FAMI_ESTRATOVIVIENDA": str}
#    )
#df['FAMI_ESTRATOVIVIENDA'].astype('category')
#print(df.columns)
#print(filtered_df.dtypes)
#for i in df.columns:
#    print([i,  df[i].dtypes]) 	

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/icfes')

#df=pd.read_sql_query('select * from datafinaldepurado LIMIT 1000',con=engine)

#df.dropna(inplace=True)

#avalaible_test=df.prueba.unique()
available_test=pd.read_sql_query('select distinct prueba from datafinaldepurado',con=engine)
available_test=available_test['prueba']

avalaible_module=["mod_comuni_escrita_punt","mod_competen_ciudad_punt","mod_lectura_critica_punt","mod_razona_cuantitat_punt","mod_ingles_punt"]

min_periodo=pd.read_sql_query('select min(periodo) from datafinaldepurado',con=engine)
min_periodo=min_periodo.loc[0,'min']
max_periodo=pd.read_sql_query('select max(periodo) from datafinaldepurado',con=engine)
max_periodo=max_periodo.loc[0,'max']
periodos=pd.read_sql_query('select distinct periodo from datafinaldepurado',con=engine)
periodos=periodos['periodo']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    html.H1("ICFES Test Dashboard", style={'text-align':'center'}, id='Title'),

    html.Div([
        html.Label('Test'),
        dcc.Dropdown(
            id='filter-test',
            options=[{'label': i, 'value': i} for i in available_test],
            value='SaberPro'
        )
    ]),


    html.Div([
        html.Label('Module'),
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i} for i in avalaible_module],
            value="mod_comuni_escrita_punt"
        )
    ]),    

    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=min_periodo, #df['periodo'].min(),
        max=max_periodo, #df['periodo'].max(),
        value=min_periodo, #df['periodo'].min(),
        marks={str(year): str(year) for year in periodos}, #df['periodo'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('filter-test', 'value'),
    Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_figure(selected_test,selected_year, selected_mod):
    #filtered_df = df[(df.periodo == selected_year) & (df.prueba == selected_test)]
	
    query = '''
    select fami_estratovivienda, '''+selected_mod+''' 
    from datafinaldepurado 
    where prueba = \''''+ selected_test + '''\' and periodo = ''' + str(selected_year)+'''
    '''
    print(query)
    filtered_df = pd.read_sql_query(query,con=engine)
    filtered_df.dropna(inplace=True)
    print(filtered_df.shape)
    var_partition = "fami_estratovivienda"
    fig = px.box(filtered_df, x=var_partition, y=selected_mod, color=var_partition)
    
    fig.update_layout(transition_duration=2)
    fig.update_yaxes(title=selected_mod) 

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)