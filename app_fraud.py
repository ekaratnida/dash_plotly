# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from transformers import AutoModelForCausalLM, AutoTokenizer
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_csv('data2/fraudTrain.csv')
fig1 = go.Figure(data=[
    go.Table(
        header=dict
        (
            values=list(df.columns),
            fill_color='paleturquoise',
            align='left'
        ),
        cells=dict
        (
            values=df.iloc[0:5].transpose().values.tolist(),
            fill_color='lavender',
            align='left'
        )
    )
])

fig2 = go.Figure(go.Indicator(
    mode = "number",
    value = df.shape[0],
    title = {'text': "df size"},
    domain = {'x': [0, 1], 'y': [0, 1]}
))

app.layout = html.Div([ 

    html.Div(children=[
        html.H1(children='Hello Dash'),
        html.Div(children='''
            Dash: A web application framework for your data.
        '''),
        dcc.Graph(
            id='fig1',
            figure=fig2
        ),
        
        dcc.Graph(
            id='fig2',
            figure=fig1
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)