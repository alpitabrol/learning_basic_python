import dash
import dash_core_components as dcc
import dash_html_components as html
 
external_stylesheets = [‘https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
 
app.layout = html.Div(children=[
html.H1(children=’Weather Dashboard’),
 
html.Div(children=’’’
Dash: A web application framework for Python.
 ‘’’),
 
 dcc.Graph(
 id=’example-graph’,
 figure={
 ‘data’: [
 {‘x’: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ‘y’: [60.56, 150.43, 76.98, 80.49, 250.80, 110.56, 80.33,
 20.44, 15.32, 90.11, 150.67, 150.55], ‘type’: ‘bar’, ‘name’: ‘Expected Rain’},
 {‘x’: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ‘y’: [40.09, 128.82, 51.57, 88.53, 295.47, 47.94, 42.05,
 3.41, 14.4, 113.65, 226.95, 142.51], ‘type’: ‘bar’, ‘name’: Actual Rain’},
 ],
 ‘layout’: {
 ‘title’: ‘Rainfall in SL in 2016’
 }
 }
 )
 ])
 
if __name__ == ‘__main__’:
 app.run_server(debug=True)

