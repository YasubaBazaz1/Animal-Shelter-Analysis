from dash import dash
from model import * 
import dash_bootstrap_components as dbc

# Use a newer, working version of Font Awesome
FONT_AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME], title="MyDashApp")

app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
