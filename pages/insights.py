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
            model it seems that fashion is not a great category to go into when starting a kickstarter.
            The biggest factors seem to be whether or not your Kickstater is "staff picked" or in the
            "Dance" category.
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