"""Self updating airline flights dashboard per year. The year can be selected.
The dashboard runs at the following URL: http://127.0.0.1:8002/"""

import pandas as pd
import plotly.express as px
import dash

from dash import html
from dash import dcc

from dash.dependencies import Input, Output

low_memory = False

airline_data = pd.read_csv('airline_2m.csv',
                           encoding = "ISO-8859-1",
                           dtype = {'Div1Airport': str,
                                    'Div1TrailNum':str,
                                    'Div2Airport': str,
                                    'Div2TrailNum':str })

app = dash.Dash()

app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style={'textAlign': 'center',
                                            'font-size':40}),
                                html.Div(["Input: ", dcc.Input(id='input-yr', value='2010',
                                                               type='number', style={'height':'50px',
                                                                                     'font-size': 35}),],
                                         style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='bar-plot')),
                                ])


@app.callback(Output(component_id='bar-plot', component_property='figure'),
              Input(component_id='input-yr', component_property='value'))

def get_graph(entered_year):

    df = airline_data[airline_data['Year'] ==int(entered_year)]
    g1 = df.groupby(['Reporting_Airline'])['Flights'].sum().nlargest(10).reset_index()

    fig1 = px.bar(g1, x='Reporting_Airline', y='Flights', title='Top 10 airline carrier in year' +
                  str(entered_year) + ' in terms of number of flights')

    fig1.update_layout()
    return fig1

if __name__ == '__main__':
    #app.run_server(port=8002, host='127.0.0.1', debug=True)

