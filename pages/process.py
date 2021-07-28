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
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            What do we do as Data Scientists?
            We look at the data, do some cleaning and feature engineering, and run some predictive modeling
            to train a model to create some kind of output.
            The goal of this model is to predict whether or not a Kickstarter campaign will be successful.
            We looked at what features were the most important and isolated those and ran through a RandomSearch
            to produce our current working model.

            Originally we started out with a 5 layer neural network, but constantly running models proved
            to us that the simpler the better in this case.

            Our baseline accuracy was a 61% while our model was easily achieving 75% accuracy or higher.

            """
        ),

    ],
)

layout = dbc.Row([column1])