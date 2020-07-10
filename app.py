import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('data/data-final.csv')

available_test=["MOD_COMUNI_ESCRITA_PUNT","MOD_COMPETEN_CIUDADA_PUNT","MOD_LECTURA_CRITICA_PUNT","MOD_RAZONA_CUANTITAT_PUNT","MOD_INGLES_PUNT"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i} for i in available_test],
            value="MOD_INGLES_PUNT"
        ),

    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['PERIODO'].min(),
        max=df['PERIODO'].max(),
        value=df['PERIODO'].min(),
        marks={str(year): str(year) for year in df['PERIODO'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value'),
    Input('yaxis-column', 'value')])
def update_figure(selected_year, punt):
    filtered_df = df[df.PERIODO == selected_year]

    fig = px.box(filtered_df, x="FAMI_ESTRATOVIVIENDA", y=punt, color="FAMI_ESTRATOVIVIENDA")

    fig.update_layout(transition_duration=5)

    fig.update_yaxes(title=punt) 


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)