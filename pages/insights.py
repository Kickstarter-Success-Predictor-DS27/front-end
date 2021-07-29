# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             ## Insights


#             """
#         ),

#     ],
# )

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
layout = html.Div([body])