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
        ])

@app.callback(
    Output('feature-graphic2', 'figure'),
    [Input('mu', 'value'),
     Input('sd', 'value'),
     Input('z', 'value')])
def update_graph2(mu,sd,z):
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
    app.run_server()
