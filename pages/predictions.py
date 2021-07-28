# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import sklearn
#import tensorflow as tf
#import keras as ks

#import numpy as np

# Imports from this application
from app import app
#from joblib import load

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
#loc = './assets/base_model.h5' --> base model
#model = ks.models.load_model(loc) --> load keras model

loc1 = './assets/clf_model.h5'
model = sklearn.joblib.load(loc1)


body = dbc.Container([

        ## Slider incase we decide it looks better
        # dcc.Markdown('''#### Goal (USD)'''),
        # dcc.Slider(
        #     id='goal',
        #     min=1,
        #     max=100000000,
        #     step=50000,
        #     value=4590,
        #     ),
        # dcc.Markdown('', id='goal-container',
        #              style ={'textAlign': 'center',
        #                      'font-size': 18},
        #              className='mb-5'),

        dcc.Markdown('''#### Goal (USD)''',
        style ={'textAlign': 'center', 'font-size': 30}),

        html.Div(
            children=[dcc.Input(
            id='goal',
            type='text',
            value = 4590,
            placeholder="Don't Leave Blank",
            style ={'textAlign': 'center','font-size': 30},
            className='mb-5'
        )],
        style=dict(display='flex', justifyContent="center", className="h-50")
        )
        ])

body2 = dbc.Container([
            dcc.Markdown('',id='prediction-content', style={
            'textAlign':'center','font-size':30}),
])


column1 = dbc.Col(
    [   
        ## Commenting out instead of deleting just ot save time
        # dcc.Markdown('''#### Goal (USD)'''),
        # dcc.Slider(
        #     id='goal',
        #     min=0,
        #     max=100000000,
        #     step=50000,
        #     value=4590,
        # ),
        # dcc.Markdown('', id='goal-container'),

        ## Feature leakage so keeping it incase we need it layer
        # dcc.Markdown('''#### Pledged Amount (USD)'''),
        # dcc.Slider(
        #     id='usd_pledged',
        #     min=0,
        #     max=9000000,
        #     step=1000,
        #     value=200000,
        # ),
        # dcc.Markdown('', id='usd_pledged-container'),

        # dcc.Markdown('''#### Backers Count'''),
        # dcc.Slider(
        #     id='backers_count',
        #     min=0,
        #     max=60000,
        #     step=1000,
        #     value=250,
        # ),
        # dcc.Markdown('', id='backers_count-container'),

        dcc.Markdown('''#### Dance'''),
        dbc.Label('Is this Dance Related?'),
        dcc.Dropdown(
            id='Dance',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                      ],
            value=0,
            className='mb-5',
            ),

        dcc.Markdown('''#### Fashion'''),
        dbc.Label('Is this Fashion Related?'),
        dcc.Dropdown(
            id='Fashion',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                      ],
            value=0,
            className='mb-5',
            ),

        dcc.Markdown('''#### Film & Video'''),
        dbc.Label('Is this Film & Video Related?'),
        dcc.Dropdown(
            id='FilmVideo',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                      ],
            value=0,
            className='mb-5',
            ),        
        ],
    )

column2 = dbc.Col(
    [
        dcc.Markdown('''#### Game'''),
        dbc.Label('Is this Game Related?'),
        dcc.Dropdown(
            id='Games',
            options=[{'label': 'Yes', 'value': 1},
                     {'label': 'No', 'value': 0},
                      ],
            value=0,
            className='mb-5',
            ), 

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

        # Removed due to feature leakage
        # dcc.Markdown('''#### Spotlight'''),
        # dbc.Label('In the Spotlight?'),
        # dcc.Dropdown(
        #     id='spotlight_2',
        #     options=[{'label': 'Yes', 'value': 1},
        #              {'label': 'No', 'value': 0},
        #              ],
        #     value=1,
        #     className='mb-5'
        # ),
        # #dcc.Markdown('', id='spotlight_2'),        

        ],
    
    )
## Not needed after moving features around
# column3 =  dbc.Col([
#             # dcc.Markdown('''#### Predicted Status'''),
            
#             dcc.Markdown('',id='prediction-content', style={
#             'textAlign':'center',
#             'font-size':30}),
            
#             #html.Img(src='assets/confusion_plot_rf.png', className='img-fluid')
# ])   

# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-container', 'children'),
    [dash.dependencies.Input('goal', 'value')])
def update_output(value):
    return 'Goal(USD) = "{}"'.format(value)

## May or may not need depending on model.
# @app.callback(
#     dash.dependencies.Output('backers_count-container', 'children'),
#     [dash.dependencies.Input('backers_count', 'value')])
# def update_output(value):
#     return 'Backers Count = "{}"'.format(value)

# @app.callback(
#     dash.dependencies.Output('usd_pledged-container', 'children'),
#     [dash.dependencies.Input('usd_pledged', 'value')])
# def update_output(value):
#     return 'Pledged Amount (USD) = "{}"'.format(value)

# Callback for the prediction container
# @app.callback(
#     Output('prediction-content','children'),
#     [ Input('backers_count', 'value'),
#       Input('goal', 'value'),
#       Input('usd_pledged', 'value'),
#       Input('spotlight_2', 'value'),
#       Input('staff_pick_2', 'value'),
#       Input('is_starrable_2', 'value'),
#      ])

# def predict(backers_count, goal, usd_pledge, spotlight_2, staff_pick_2, is_starrable_2):
#         df = pd.DataFrame(columns=['backers_count', 'goal', 'usd_pledged', 'spotlight_2', 'staff_pick_2', 'is_starrable_2'],
#         data=[[backers_count, goal, usd_pledge, spotlight_2, staff_pick_2, is_starrable_2]])
#         df = np.array(df).astype('float32')
#         df = df[:2]
#         y_pred = model.predict(df)[0][0]
#         y_round = round(y_pred)
#         print(y_pred)
#         if y_round == 1:
#             return "This campaign is likely to be successful"
#         else:
#             return "This campaign is likely to fail."
 
@app.callback(
    Output('prediction-content','children'),
    [ Input('goal', 'value'),
      Input('Dance', 'value'),
      Input('Fashion', 'value'),
      Input('FilmVideo', 'value'),
      Input('Games', 'value'),
      Input('staff_pick_2', 'value'),
      Input('is_starrable_2', 'value'),
     ])

def predict(goal, Dance, Fashion, FilmVideo, Games, staff_pick_2, is_starrable_2):
        df = pd.DataFrame(columns=['goal', 'Dance', 'Fashion', 'Film & Video', 'Games', 'staff_pick_2', 'is_starrable_2'],
        data=[[goal, Dance, Fashion, FilmVideo, Games, staff_pick_2, is_starrable_2]])
        #df = np.array(df).astype('float32')
        #df = df[:2]
        y_pred = model.predict(df)[0]
        y_round = round(y_pred)
        #print(df) --> used this for testing outputs
        #print(y_pred)
        if y_round == 1:
            return "This campaign is likely to succeed"
        else:
            return "This campaign is likely to fail."

#layout = dbc.Row([column1, column2, column3])

layout = dbc.Row([body, column1, column2, body2])