import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app


# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             Trying to figure out whether your Kickstarter will be a success?
#             Use this app to figure out!
#             """
#         ),
#         dcc.Link(
#             dbc.Button('Calculator', color='primary'), href='/predictions')
#     ],
#     md=4,
# )

# column2 = dbc.Col(
#     [
#         html.Img(src='kickstarter.jpeg', className='img-fluid')
#     ]
# )

# layout = dbc.Row([column1, column2])

# layout = html.Div(
#     [
#         html.Hr(),
#         dbc.Row(
#             [
#             dcc.Link(
#                 dbc.Button('Calculator',
#                             color='primary'), href='/predictions'),
                            
#             ],
#             style={'width': '96%', 'padding-left': '3%', 'padding-right': '1%'},
#         ),
#         html.Hr(),
#         dbc.Row(
#             [
#               dcc.Markdown(
#             """
#             Trying to figure out whether your Kickstarter will be a success?
#             Use this app to figure out!
#             """
#             ),
#             ],
#             style={'width': '96%','padding-left': '3%', 'padding-right': '1%'},
#         ),
#     ], 
#     style={
#         # 'background-image':'url("/assets/background.jpg")'
#         'text-align': 'center'
#     }
# )

body = dbc.Container([
dbc.Row(
            [
            html.Img(src='assets/kickstarter-logo.jpeg',
                     className='img-fluid', 
                     style={'height':'50%', 'width':'50%'})
            ], justify="center", align="center", className="h-50"  
       ),

dbc.Row(
            [
            dcc.Markdown(
            """
            ## NOT ALL CROWDFUNDING IS THE SAME!
            """,
            ),
            ], justify="center", align="center", className="h-50"
            ),

dbc.Row(
            [
            dcc.Markdown(
            """
            There are many features that go into determining whether or not 
            a Kickstarter campaign will be successful.
            """,
            ),
            ], justify="center", align="center", className="h-50"
            ),

dbc.Row(
            [
            dcc.Markdown(
            """
            Have you ever wondered what's need to be a successful kickstater?
            """,
            ),
            ], justify="center", align="center", className="h-50"
            ),

dbc.Row(
            [
            dcc.Markdown(
            """
            Use the calulator below to see!
            """,
            ),
            ], justify="center", align="center", className="h-50"
            ),

dbc.Row(
            [
            dcc.Link(
                 dbc.Button('Press Me!!!!',
                             color='success',
                             block=True, 
                             #size="lg"
                             ),
                             href='/predictions',
),
            ], justify="center", align="center", className="h-50"
            )
]

)

layout = html.Div([body])