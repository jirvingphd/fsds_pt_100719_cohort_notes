import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from scipy.stats import binom, norm
import numpy as np


app = dash.Dash(name=__name__)#, static_folder='static')

# THE EXTERNAL CSS FILE REMOVES THE DASH "UNDO/REDO" BUTTON
app.css.append_css({'external_url':'static/my.css'})

app.layout = html.Div([
    
    html.Div(id='BinomialDist.py',children=[dcc.Graph(id='feature-graphic1', config={'displayModeBar': False}),
        html.Div([
        html.Div('n=',style={'width':'8%','fontSize':24,'fontStyle':'italic','float':'left','textAlign':'right','paddingRight':20}),
        dcc.Input(
            id='n',
            type='number',
            value=50,
            style={'width':'8%','fontSize':24,'float':'left'}),
        html.Div('p=',style={'width':'5%','fontSize':24,'fontStyle':'italic','float':'left','textAlign':'right','paddingRight':20}),
        html.Div(dcc.Slider(
            id='p',
            min=0,
            max=12,
            step=None,
            marks={
                0: {'label': '0', 'style': {'fontSize':18,'color': '#f50'}},
                1: {'label': '1/6', 'style': {'fontSize':18}},
                2: {'label': '1/5', 'style': {'fontSize':18}},
                3: {'label': '1/4', 'style': {'fontSize':18}},
                4: {'label': '1/3', 'style': {'fontSize':18}},
                5: {'label': '2/5', 'style': {'fontSize':18}},
                6: {'label': '1/2', 'style': {'fontSize':18}},
                7: {'label': '3/5', 'style': {'fontSize':18}},
                8: {'label': '2/3', 'style': {'fontSize':18}},
                9: {'label': '3/4', 'style': {'fontSize':18}},
                10: {'label': '4/5', 'style': {'fontSize':18}},
                11: {'label': '5/6', 'style': {'fontSize':18}},
                12: {'label': '1', 'style': {'fontSize':18,'color': '#f50'}}
            },
            included=False,
            value=6), style={'width':'65%','float':'left'})
        ])
        ]),
    html.Div(id='NormalDist1.py',children=[
        dcc.Graph(id='feature-graphic2', config={'displayModeBar': False}),
        html.Div([
        html.Div('μ=',style={'width':'8%','fontSize':24,'fontStyle':'italic',
        'float':'left','textAlign':'right','paddingRight':20}),
        dcc.Input(
            id='mu',
            type='number',
            value=0,
            style={'width':'8%','fontSize':24,'float':'left'}),
        html.Div('std =',style={'width':'7%','fontSize':24,
        'fontFamily':'symbol','float':'left','textAlign':'right',
        'paddingRight':50}),
        html.Div(dcc.Input(
            id='sd',
            type='number',
            value=1,
            style={'width':'8%','fontSize':24,'float':'left'})),
        html.Div('Show Z?',style={'width':'10%','fontSize':24,
        'fontStyle':'italic','float':'left','textAlign':'right',
        'paddingRight':30,'paddingLeft':15}),
        html.Div(dcc.RadioItems(
            id='z',
            options=[
                {'label':'Yes', 'value':1},
                {'label':'No', 'value':0},
            ],
            value=0,
            labelStyle={'display':'inline-block','fontSize':24})),
        ])
        ]),
    
    ])


## CALLBACKS

# BinomialDist.py
@app.callback(
    Output('feature-graphic1', 'figure'),
    [Input('n', 'value'),
     Input('p', 'value')])
def update_graph(n,p):
    pset = [0,0.1667,0.2,0.25,0.3333,0.4,0.5,0.6,0.6667,0.75,0.8,0.8333,1]
    x = list(range(n+1))
    y = [binom.pmf(i,n,pset[p]) for i in range(n+1)]
    return {
        'data': [go.Bar(
            x=x,
            y=y,
            width=[0.2]*(n+1),
        )],
        'layout': go.Layout(
            title='Binomial Distribution',
            margin={'l':40, 'b':40, 't':50, 'r':0}
        ),
    }
    
@app.callback(
    Output('feature-graphic2', 'figure'),
    [Input('mu', 'value'),
     Input('sd', 'value'),
     Input('z', 'value')])
def update_graph(mu,sd,z):
    x = np.linspace(mu-(4*sd),mu+(4*sd),1001)
    y = [norm.pdf(i,mu,sd) for i in x]
    zx = [mu-(3*sd),mu-(2*sd),mu-sd,mu+sd,mu+(2*sd),mu+(3*sd)]
    zy = [norm.pdf(i,mu,sd) for i in zx]
    trace0 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        hoverinfo='none'
    )
    trace1 = go.Bar(
        x = zx,
        y = zy,
        text = ['Z=-3','Z=-2','Z=-1','Z=1','Z=2','Z=3'],
        width = [0.02]*6,
        hoverinfo='text+x'
    )
    if z:
        data = [trace0,trace1]
    else:
        data = [trace0]

    return {
        'data':data,
        'layout': go.Layout(
            title='Normal Distribution',
            margin={'l':40, 'b':40, 't':50, 'r':40},
            showlegend=False
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)
