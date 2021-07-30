# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app


# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout


body = dbc.Container([
    dbc.Row([
        dcc.Markdown(
            '''
            Just a quick little note. When loading the Correlation Matrix Associated with our 
            model it seems that the largest contributor to a successful Kickstarter is going to be 
            whether or not your campaign is "Staff Picked." It means that the more spotlight and exposure
            your project has, the better chances it has at being successful. 
            '''
        ),
    ]),

    dbc.Row([
        dcc.Markdown(
            '''
            Also, setting to lofty of a goal, as in asking for too much money, can easily 
            change the outcome of your campaign.
            '''
        ),
    ]),

    dbc.Row([
            html.Img(src='assets/Corr_Matrix.png',
                     className='img-fluid', 
                     style={'height':'50%', 'width':'50%'})
            ], justify="center", align="center", className="h-50"  
       )
]
)

body1 = dbc.Container([
    dbc.Row([
        dcc.Markdown(
            '''
            We also have a graph here of our feature importances. Our category feature and whether or not
            the Kickstarter is starrable play a large part in our models performace.
            '''
        ),
    ]),

    dbc.Row([
        dcc.Markdown(
            '''
            It's no surprise either that location seems to have the least importance as the Internet
            keeps us better connected than ever before.
            '''
        ),
    ]),
    dbc.Row([
            html.Img(src='assets/Feature_importance.png',
                     className='img-fluid', 
                     style={'height':'50%', 'width':'50%'})
            ], justify="center", align="center", className="h-50"  
       )
]
)
layout = html.Div([body, body1])