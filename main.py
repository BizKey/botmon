from dash import Dash, html, dcc
import plotly.express as px

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
