import requests
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

#Document of Binance API
#https://binance-docs.github.io/apidocs/spot/en/#rolling-window-price-change-statistics

symbol = '["BTCUSDT","ETHUSDT"]' #&windowSize=10m'
api = "https://api.binance.com/api/v3/ticker?type=MINI&windowSize=1d&symbols="+symbol
btc_coin = 'BTC/USDT'
eth_coin = 'ETH/USDT'
jsonData = requests.get(api).json()
print(jsonData[0]['lastPrice'])

#price = float(jsonData['lastPrice'])
#print(price)

fig = go.Figure()

fig.add_trace(go.Indicator(
      mode = "number+delta",
      value = float(jsonData[0]['lastPrice']),
      title = btc_coin,
      number={"valueformat": '0.4f'},
      domain = {'row': 0, 'column': 0},
      delta = {'reference': float(jsonData[0]['highPrice']), 
               'relative': True, 
               'valueformat': '.4%'},
    )
)

fig.add_trace(go.Indicator(
      mode = "number+delta",
      value = float(jsonData[1]['lastPrice']),
      title = eth_coin,
      number={"valueformat": '0.4f'},
      domain = {'row': 0, 'column': 1},
      delta = {'reference': float(jsonData[1]['highPrice']), 
               'relative': True, 
               'valueformat': '.4%'}
    )
)

fig.update_layout(
    grid = {'rows': 1, 'columns': 2}
    )


app.layout = html.Div([ 

    html.Div(children=[
        html.H1(children='DADS NIDA'),
        html.Div(children='''
            Crypto Indicator
        '''),
        dcc.Graph(
            id='id1',
            figure=fig
        ),
        dcc.Interval(id="interval", interval=1*1000) # 1 sec 
    ])
])

@app.callback(
    Output('id1', 'figure'),
    [Input('interval', 'n_intervals')])
def update_data(n_intervals):

    print("interval ",n_intervals)

    jsonData = requests.get(api).json()
    #print(data)

    fig = go.Figure()

    
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = float(jsonData[0]['lastPrice']),
        title = btc_coin,
        number={"valueformat": '0.4f'},
        domain = {'row': 0, 'column': 0},
        delta = {'reference': float(jsonData[0]['highPrice']), 
                 'relative': True, 'valueformat': '.4%'}
        )
    )

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = float(jsonData[1]['lastPrice']),
        title = eth_coin,
        number={"valueformat": '0.4f'},
        domain = {'row': 0, 'column': 1},
        delta = {'reference': float(jsonData[1]['highPrice']), 
                 'relative': True, 'valueformat': '.4%'}
        )
    )

    fig.update_layout(
        grid = {'rows': 1, 'columns': 2}
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)