"""
This is the entry point for the Dash application.
No changes are needed here.
Hii
"""
import dash
import dash_bootstrap_components as dbc

from tool.layout import layout
from tool.callbacks import register_callbacks


# Initialize the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
# Add the layout
app.layout = layout()
# Add the callbacks
register_callbacks(app)
# create a server object
server = app.server # Crucial for deployment!

# Run the server
if __name__ == '__main__':
   app.run_server(debug=True)