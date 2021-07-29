# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
#import tensorflow as tf
#import keras as ks

#import numpy as np

# Imports from this application
from app import app
from joblib import load

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
#loc = './assets/base_model.h5' --> base model
#model = ks.models.load_model(loc) --> load keras model

loc1 = './assets/clf1_model.h5'
model = load(loc1)


body = dbc.Container([

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
        dcc.Markdown('''#### Category'''),
        dbc.Label('Is kind of campaign?'),
        dcc.Dropdown(
            id='sub_categories',
            options=[{'label': 'Games', 'value': 3},
                     {'label': 'Film & Video', 'value': 2},
                     {'label': 'Fashion', 'value': 1},
                     {'label': 'Dance', 'value': 0},
                      ],
            value=0,
            className='mb-5',
            ),

        dcc.Markdown('''#### Location'''),
        dbc.Label("What's the Location?"),
        dcc.Dropdown(
            id='sub_location',
            options=[{'label': 'Zambia', 'value': 64},
                     {'label': 'Viet Nam', 'value': 63},
                     {'label': 'Uruguay', 'value': 62},
                     {'label': 'United States', 'value': 61},
                     {'label': 'Uganda', 'value': 60},
                     {'label': 'Ukraine', 'value': 59},
                     {'label': 'Taiwan', 'value': 58},
                     {'label': 'Trinidad and Tobago', 'value': 57},
                     {'label': 'Turkey', 'value': 56},
                     {'label': 'Thailand', 'value': 55},
                     {'label': 'Slovakia', 'value': 54},
                     {'label': 'Singapore', 'value': 53},
                     {'label': 'Sweden', 'value': 52},
                     {'label': 'Russian Federation', 'value': 51},
                     {'label': 'Serbia', 'value': 50},
                     {'label': 'Romania', 'value': 49},
                     {'label': 'Portugal', 'value': 48},
                     {'label': 'Puerto Rico', 'value': 47},
                     {'label': 'Poland', 'value': 46},
                     {'label': 'Philippines', 'value': 45},
                     {'label': 'New Zealand', 'value': 43},
                     {'label': 'Norway', 'value': 42},
                     {'label': 'Netherlands', 'value': 41},
                     {'label': 'Malaysia', 'value': 40},
                     {'label': 'Mexico', 'value': 39},
                     {'label': 'Mali', 'value': 38},
                     {'label': 'Republic of Macedonia', 'value': 37},
                     {'label': 'Latvia', 'value': 36},
                     {'label': 'Lithuania', 'value': 35},
                     {'label': 'Korea (South)', 'value': 34},
                     {'label': 'Japan', 'value': 33},
                     {'label': 'Jordan', 'value': 32},
                     {'label': 'Jamaica', 'value': 31},
                     {'label': 'Italy', 'value': 30},
                     {'label': 'Iceland', 'value': 29},
                     {'label': 'India', 'value': 28},
                     {'label': 'Isreal', 'value': 27},
                     {'label': 'Ireland', 'value': 26},
                     {'label': 'Hungary', 'value': 25},
                     {'label': 'Haiti', 'value': 24},
                     {'label': 'Hong Kong', 'value': 23},
                     {'label': 'Greece', 'value': 22},
                     {'label': 'Ghana', 'value': 21},
                     {'label': 'United Kingdom', 'value': 20},
                     {'label': 'France', 'value': 19},
                     {'label': 'Fiji', 'value': 18},
                     {'label': 'Finland', 'value': 17},
                     {'label': 'Ethiopia', 'value': 16},
                     {'label': 'Spain', 'value': 15},
                     {'label': 'Egypt', 'value': 14},
                     {'label': 'Algeria', 'value': 13},
                     {'label': 'Denmark', 'value': 12},
                     {'label': 'Germany', 'value': 11},
                     {'label': 'Czech Republic', 'value': 10},
                     {'label': 'China', 'value': 9},
                     {'label': "Côte d'Ivoire", 'value': 8},
                     {'label': 'Switzerland', 'value': 7},
                     {'label': 'Canada', 'value': 6},
                     {'label': 'Bulgaria', 'value': 5},
                     {'label': 'Belgium', 'value': 4},
                     {'label': 'Bosnia and Herzegovina', 'value': 3},
                     {'label': 'Australia', 'value': 2},
                     {'label': 'Austria', 'value': 1},
                     {'label': 'Argentina', 'value': 0},
                     ],
            value=61,
            className='mb-5',
            ),

        ],
    )

column2 = dbc.Col([

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
      Input('sub_categories', 'value'),
      Input('sub_location', 'value'),
      Input('staff_pick_2', 'value'),
      Input('is_starrable_2', 'value'),
     ])

def predict(goal, sub_categories, sub_locations, staff_pick_2, is_starrable_2):
        df = pd.DataFrame(columns=['goal', 'sub_categories', 'sub_location', 'staff_pick_2', 'is_starrable_2'],
        data=[[goal, sub_categories, sub_locations, staff_pick_2, is_starrable_2]])
        #df = np.array(df).astype('float32')
        #df = df[:2]
        y_pred = model.predict(df)[0]
        y_round = round(y_pred)
        print(df) #--> used this for testing outputs
        print(y_pred)
        if y_round == 1:
            return "This campaign is likely to succeed"
        else:
            return "This campaign is likely to fail."

#layout = dbc.Row([column1, column2, column3])

layout = dbc.Row([body, column1, column2, body2])