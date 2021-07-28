# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, insights, process

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
# navbar = dbc.NavbarSimple(
#     brand='Kickstarter-Success-Predictor',
#     brand_href='/', 
#     children=[
#         dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
#         dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
#         dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
#     ],
#     sticky='top',
#     color='light', 
#     light=True, 
#     dark=False
# )

navbar = dbc.DropdownMenu(
    label='Menu',
    bs_size="lg",
    color="success",
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')),
        dbc.DropdownMenuItem(divider=True), 
        dbc.NavItem(dcc.Link('Home', href='/', className='nav-link')),
    ],
    className="mb-1",
    right=True
)

navbar = dbc.NavbarSimple(
    children=[
    dbc.DropdownMenu(
    label='Menu',
    bs_size="lg",
    color="success",
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')),
        dbc.DropdownMenuItem(divider=True), 
        dbc.NavItem(dcc.Link('Home', href='/', className='nav-link')),
    ],
    className="mb-1",
    right=True
)
    ],
    brand="Kickstarter Success",
    brand_href="/",
    color="success",
    dark=False,
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Mayra Artis', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'), 
                                    href='https://github.com/martis407'),
                                html.A(html.I(className='fab fa-linkedin mr-1'),
                                    href='https://www.linkedin.com/in/mayra-artis-81471252/'), 
                                html.A(html.I(className='fas fa-envelope-square mr-1'),
                                    href='mailto:mayra.artis@gmail.com'),  
                            ], 
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Ian Knight', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'),
                                    href='https://github.com/iknight7000'),
                                html.A(html.I(className='fab fa-linkedin mr-1'),
                                    href='https://www.linkedin.com/in/ianknight480/'), 
                                html.A(html.I(className='fas fa-envelope-square mr-1'),
                                    href='mailto:ianknight7000@gmail.com'),
                            ], 
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Jeremiah Evangelista', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'),
                                    href='https://github.com/mramputatoes'),
                                html.A(html.I(className='fab fa-linkedin mr-1'),
                                    href=
                                    'https://www.linkedin.com/in/jeremiah-evangelista-6ba928157/'), 
                                html.A(html.I(className='fas fa-envelope-square mr-1'),
                                    href='mailto:mramputatoes@gmail.com'),
                            ], 
                            className='lead'
                        )
                    ]
                ),
            ]
        )
    ]
)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navbar,
        dbc.Container(id='page-content', className='mt-4'),
        html.Hr(),
        footer
    ],
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

if __name__ == '__main__':
    app.run_server(debug=True)
