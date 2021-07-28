# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import tensorflow as tf
import keras as ks
import pandas as pd
import numpy as np

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
loc = './assets/base_model.h5'
model = ks.models.load_model(loc)

column1 = dbc.Col(
    [
        dcc.Markdown('''#### Goal (USD)'''),
        dcc.Slider(
            id='goal',
            min=0,
            max=100000000,
            step=50000,
            value=4590,
        ),
        dcc.Markdown('', id='goal-container'),


        dcc.Markdown('''#### Pledged Amount (USD)'''),
        dcc.Slider(
            id='usd_pledged',
            min=0,
            max=9000000,
            step=1000,
            value=200000,
        ),
        dcc.Markdown('', id='usd_pledged-container'),


        dcc.Markdown('''#### Backers Count'''),
        dcc.Slider(
            id='backers_count',
            min=0,
            max=60000,
            step=1000,
            value=250,
        ),
        dcc.Markdown('', id='backers_count-container'),
        ],
    )

column2 = dbc.Col(
    [
        dcc.Markdown('''#### Starrable?'''),
        dbc.Label('Starrable?'),
        dcc.Dropdown(
            id='is_starrable_2',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                      ],
            value=1,
            className='mb-5',
        ),    
        #dcc.Markdown('', id='is_starrable_2'),


        dcc.Markdown('''#### Staff Pick'''),
        dbc.Label('Staff Picked?'),
        dcc.Dropdown(
            id='staff_pick_2',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                     ],
            value=1,
            className='mb-5'
        ),
        #dcc.Markdown('', id='staff_pick_2'),


        dcc.Markdown('''#### Spotlight'''),
        dbc.Label('In the Spotlight?'),
        dcc.Dropdown(
            id='spotlight_2',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                     ],
            value=1,
            className='mb-5'
        ),
        #dcc.Markdown('', id='spotlight_2'),        

        ],
    
    )

column3 =  dbc.Col([
            # dcc.Markdown('''#### Predicted Status'''),
            
            dcc.Markdown('',id='prediction-content', style={
            'textAlign':'center',
            'font-size':30}),
            
            #html.Img(src='assets/confusion_plot_rf.png', className='img-fluid')
])   

# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-container', 'children'),
    [dash.dependencies.Input('goal', 'value')])
def update_output(value):
    return 'Goal(USD) = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('backers_count-container', 'children'),
    [dash.dependencies.Input('backers_count', 'value')])
def update_output(value):
    return 'Backers Count = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('usd_pledged-container', 'children'),
    [dash.dependencies.Input('usd_pledged', 'value')])
def update_output(value):
    return 'Pledged Amount (USD) = "{}"'.format(value)

# Callback for the prediction container
@app.callback(
    Output('prediction-content','children'),
    [ Input('backers_count', 'value'),
      Input('goal', 'value'),
      Input('usd_pledged', 'value'),
      Input('spotlight_2', 'value'),
      Input('staff_pick_2', 'value'),
      Input('is_starrable_2', 'value'),
     ])

# backers_count=0
# goal = 10000000
# usd_pledge = 1000000
# spotlight_2 = 0.0
# staff_pick_2 = 0.0
# is_starrable_2 = 0.0

# column3 =  dbc.Col([ 
    
# ])

# df = pd.DataFrame(columns=['backers_count', 'goal', 'usd_pledged', 'spotlight_2','staff_pick_2', 'is_starrable_2'],
# data=[[backers_count, goal, usd_pledge, spotlight_2, staff_pick_2, is_starrable_2]])
# df = np.array(df).astype('float32')
# #df = df[:2]
# y_pred = model.predict(df)
# #y_round = round(y_pred)
# #y_round
# print(y_pred)

def predict(backers_count, goal, usd_pledge, spotlight_2, staff_pick_2, is_starrable_2):
        df = pd.DataFrame(columns=['backers_count', 'goal', 'usd_pledged', 'spotlight_2', 'staff_pick_2', 'is_starrable_2'],
        data=[[backers_count, goal, usd_pledge, spotlight_2, staff_pick_2, is_starrable_2]])
        df = np.array(df).astype('float32')
        df = df[:2]
        y_pred = model.predict(df)[0][0]
        y_round = round(y_pred)
        print(y_pred)
        if y_round == 1:
            return "This campaign is likely to be successful"
        else:
            return "This campaign is likely to fail."
 
layout = dbc.Row([column1, column2, column3])
