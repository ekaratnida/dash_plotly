from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-state-example',
        #value='Where do I live?',
        style={'width': '100%', 'height': 200},
    ),
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})
])

import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

from transformers import pipeline


@callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        #data = query(value)[0]['generated_text']
        #classifier = pipeline("ner")
        #data = classifier(value)
        classifier = pipeline("token-classification", model = "vblagoje/bert-english-uncased-finetuned-pos")
        value = classifier("Hello I'm Omar and I live in Zürich.")
        return 'You have entered: \n\n{}'.format(value)

if __name__ == '__main__':
    app.run(debug=True)
