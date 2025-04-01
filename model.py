from data_cleaning import animal_data
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Data Processing
animal_data['intake_date'] = pd.to_datetime(animal_data['intake_datetime']).dt.date
pets_per_day = round(len(animal_data) / len(animal_data['intake_date'].unique()), 0)


card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 40,
    "margin": "auto",
}


card1 = dbc.CardGroup([
    dbc.Card(
        dbc.CardBody(
            [
                html.H5(pets_per_day, className="class-title"), 
                html.P("Number of animals left at centre daily", className="card-text")
            ]
        )
    ),
    dbc.Card(
        html.I(className="fas fa-cat", style=card_icon),  
        class_name="bg-info",
        style={"maxWidth": "40%"}
    ),
], className="mt-4 shadow")

# Average Days in Shelter
avg_days_in_shelter = round(animal_data['time_in_shelter_days'].mean(), 1)

# Card for Average Days in Shelter
card2 = dbc.CardGroup([
    dbc.Card(
        dbc.CardBody(
            [
                html.H5(avg_days_in_shelter, className="class-title"), 
                html.P("Avg no. of days spent in shelter", className="card-text")
            ]
        )
    ),
    dbc.Card(
        html.I(className="fas fa-calendar-day", style=card_icon),  
        class_name="bg-info",
        style={"maxWidth": "40%"}
    ),
], className="mt-4 shadow")

# Adoption Rate
adoption_rate = round(animal_data['outcome_type'].value_counts()*100 / len(animal_data), 0)['Adoption']

# Card for Adoption Rate
card3 = dbc.CardGroup([
    dbc.Card(
        dbc.CardBody(
            [
                html.H5(str(adoption_rate) + "%", className="class-title"), 
                html.P("Adoption rate of animals in shelter", className="card-text")
            ]
        )
    ),
    dbc.Card(
        html.I(className="fas fa-heart", style=card_icon),  
        class_name="bg-info",
        style={"maxWidth": "40%"}
    ),
], className="mt-4 shadow")


animal_type_pie = px.pie(animal_data['animal_type'].value_counts().reset_index(), values='animal_type', names='index', title='Animals Received')
outcomes = animal_data['outcome_type'].value_counts().reset_index()
outcome_bar = px.bar(animal_data['outcome_type'].value_counts().reset_index().sort_values(by='outcome_type', ascending=True), x='outcome_type', y='index', title='Outcome Type Of Animals')
age_histogram = px.scatter(animal_data, x="age_upon_intake_(years)", y="time_in_shelter_days", color="animal_type", title='Time Spent in Shelter (Days)')

layout = html.Div([
    html.H1(" 🐶 Animal Shelter Analysis 🐶 ", style={'textAlign': 'center'}),
    html.P("Analysis done on Austin's Animal Shelter", style={'textAlign': 'center'}),

    # First row (card section)
    html.Div(dbc.Row([dbc.Col(card1), dbc.Col(card2), dbc.Col(card3)]), style={"marginBottom": "100px"}),  

    # Second row (graphs section)
    html.Div(dbc.Row([
        dbc.Col(dcc.Graph(id='pie-graph', figure=animal_type_pie, style={'width': '40vh', 'height': '50vh'})),
        dbc.Col(dcc.Graph(id='bar-graph', figure=outcome_bar, style={'width': '70vh', 'height': '50vh'})),
        dbc.Col(dcc.Graph(id='age-graph', figure=age_histogram, style={'width': '70vh', 'height': '50vh'}))
    ]), style={'textAlign': 'center'})
])