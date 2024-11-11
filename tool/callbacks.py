"""
This file is optional, if prefered the callbacks can be defined in the layout.py file too with some modifications.
"""
from dash import Dash, Input, Output, State



def register_callbacks(app:Dash):
   @app.callback(
      [Output("dummy-output", "children")],
      [Input("dummy-button", "n_clicks")],
      )
   def dummy_button_callback(n_dummy_button_clicks):
      if n_dummy_button_clicks is None:
         return "",
      elif n_dummy_button_clicks % 2 == 0:
         return "O.o",
      else:
         return "o.O",
