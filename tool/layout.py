from dash import html, dcc
import dash_bootstrap_components as dbc

def layout():
   return html.Div([
      html.H1("Hello there!"),
      html.H2("This is a simple Dash app with a Bootstrap theme."),
      dbc.Button("Click me!", id="dummy-button"),
      html.Div(id="dummy-output", style={"justify-content": "center", "display": "flex", "fontSize": "200px"})
   ])