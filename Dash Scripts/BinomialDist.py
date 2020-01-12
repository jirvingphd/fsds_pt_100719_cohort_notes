import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from scipy.stats import binom

app = dash.Dash(name=__name__)#, static_folder='static')

# THE EXTERNAL CSS FILE REMOVES THE DASH "UNDO/REDO" BUTTON
app.css.append_css({'external_url':'static/my.css'})

app.layout = html.Div([
        dcc.Graph(id='feature-graphic1', config={'displayModeBar': False}),
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
        ])

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
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
