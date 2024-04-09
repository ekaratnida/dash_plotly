from dash_extensions import WebSocket
from dash_extensions.enrich import html, dcc, Output, Input, DashProxy

# Create small example app.
app = DashProxy(__name__)

app.layout = html.Div([
    WebSocket(id="ws", url="ws://127.0.0.1:5000/random_data"),
    html.Div(id="message")
])

@app.callback(Output("message", "children"), [Input("ws", "message")])
def message(e):
    return f"Response from websocket: {e["data"]}"
    
if __name__ == "__main__":
    print("Website")
    app.run_server()