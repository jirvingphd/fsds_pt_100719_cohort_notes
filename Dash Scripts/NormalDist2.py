import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
from scipy.stats import norm

app = dash.Dash(name=__name__)#, static_folder='static')

# THE EXTERNAL CSS FILE REMOVES THE DASH "UNDO/REDO" BUTTON
app.css.append_css({'external_url':'static/my.css'})

app.layout = html.Div([
        dcc.Graph(id='feature-graphic3', config={'displayModeBar': False}),
        html.Div([
        html.Div('μ=',style={'width':'8%','fontSize':24,'fontStyle':'italic',
        'float':'left','textAlign':'right','paddingRight':20,'color':'#1f77b4'}),
        dcc.Input(
            id='mu1',
            type='number',
            value=0,
            style={'width':'8%','fontSize':24,'float':'left','color':'#1f77b4'}),
        html.Div('std =',style={'width':'7%','fontSize':24,
        'fontFamily':'symbol','float':'left','textAlign':'right',
        'paddingRight':50,'color':'#1f77b4'}),
        html.Div(dcc.Input(
            id='sd1',
            type='number',
            value=1,
            style={'width':'8%','fontSize':24,'float':'left','color':'#1f77b4'})),
        html.Div('Show Z?',style={'width':'10%','fontSize':24,
        'fontStyle':'italic','float':'left','textAlign':'right',
        'paddingRight':30,'paddingLeft':15,'color':'#1f77b4'}),
        html.Div(dcc.RadioItems(
            id='z1',
            options=[
                {'label':'Yes', 'value':1},
                {'label':'No', 'value':0},
            ],
            value=0,
            labelStyle={'display':'inline-block','fontSize':24,'color':'#1f77b4'})),
        ]),

        html.Div([
        html.Div('μ=',style={'width':'8%','fontSize':24,'fontStyle':'italic',
        'float':'left','textAlign':'right','paddingRight':20,'color':'#2ca02c'}),
        dcc.Input(
            id='mu2',
            type='number',
            value=0,
            style={'width':'8%','fontSize':24,'float':'left','color':'#2ca02c'}),
        html.Div('std =',style={'width':'7%','fontSize':24,
        'fontFamily':'symbol','float':'left','textAlign':'right',
        'paddingRight':50,'color':'#2ca02c'}),
        html.Div(dcc.Input(
            id='sd2',
            type='number',
            value=1,
            style={'width':'8%','fontSize':24,'float':'left','color':'#2ca02c'})),
        html.Div('Show Z?',style={'width':'10%','fontSize':24,
        'fontStyle':'italic','float':'left','textAlign':'right',
        'paddingRight':30,'paddingLeft':15,'color':'#2ca02c'}),
        html.Div(dcc.RadioItems(
            id='z2',
            options=[
                {'label':'Yes', 'value':1},
                {'label':'No', 'value':0},
            ],
            value=0,
            labelStyle={'display':'inline-block','fontSize':24})),
        ],style={'clear':'both','paddingTop':8,'color':'#2ca02c'})
        ])

@app.callback(
    Output('feature-graphic3', 'figure'),
    [Input('mu1', 'value'),
     Input('sd1', 'value'),
     Input('z1', 'value'),
     Input('mu2', 'value'),
      Input('sd2', 'value'),
      Input('z2', 'value')])
def update_graph3(mu1,sd1,z1,mu2,sd2,z2):
    minx=min((mu1-4*sd1,mu2-4*sd2))
    maxx=max((mu1+4*sd1,mu2+4*sd2))
    x1 = np.linspace(minx,maxx,1001)
    y1 = [norm.pdf(i,mu1,sd1) for i in x1]
    zx1 = [mu1-(3*sd1),mu1-(2*sd1),mu1-sd1,mu1+sd1,mu1+(2*sd1),mu1+(3*sd1)]
    zy1 = [norm.pdf(i,mu1,sd1) for i in zx1]
    trace10 = go.Scatter(
        x=x1,
        y=y1,
        mode='lines',
        hoverinfo='none',
        line={'color':'rgb(31, 119, 180)'}
    )
    trace11 = go.Bar(
        x = zx1,
        y = zy1,
        text = ['Z=-3','Z=-2','Z=-1','Z=1','Z=2','Z=3'],
        width = [0.02]*6,
        hoverinfo='text+x',
        marker = {'color':'#ff7f0e'}
    )
    x2 = np.linspace(minx,maxx,1001)
    y2 = [norm.pdf(i,mu2,sd2) for i in x2]
    zx2 = [mu2-(3*sd2),mu2-(2*sd2),mu2-sd2,mu2+sd2,mu2+(2*sd2),mu2+(3*sd2)]
    zy2 = [norm.pdf(i,mu2,sd2) for i in zx2]
    trace20 = go.Scatter(
        x=x2,
        y=y2,
        mode='lines',
        hoverinfo='none',
        line={'color':'rgb(44,160,44)'}
    )
    trace21 = go.Bar(
        x = zx2,
        y = zy2,
        text = ['Z=-3','Z=-2','Z=-1','Z=1','Z=2','Z=3'],
        width = [0.02]*6,
        hoverinfo='text+x',
        marker = {'color':'#d62728'}
    )
    if z1 and z2:
        data = [trace20,trace21,trace10,trace11]
    elif z1:
        data = [trace20,trace10,trace11]
    elif z2:
        data = [trace20,trace21,trace10]
    else:
        data = [trace20,trace10]

    return {
        'data':data,
        'layout': go.Layout(
            title='Normal Distribution',
            margin={'l':40, 'b':40, 't':50, 'r':40},
            showlegend=False,
            barmode='overlay'
        )
    }

if __name__ == '__main__':
    app.run_server()
