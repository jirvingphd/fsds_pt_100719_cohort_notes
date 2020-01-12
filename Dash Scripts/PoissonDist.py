import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from scipy.stats import poisson

app = dash.Dash(name=__name__)#, static_folder='static')

# THE EXTERNAL CSS FILE REMOVES THE DASH "UNDO/REDO" BUTTON
app.css.append_css({'external_url':'static/my.css'})

app.layout = html.Div([
        dcc.Graph(id='feature-graphic4', config={'displayModeBar': False}),
        html.Div([
        html.Div('μ=',style={'width':'8%','fontSize':24,'fontStyle':'italic','float':'left','textAlign':'right','paddingRight':20}),
        dcc.Input(
            id='mu',
            type='number',
            value=10,
            style={'width':'8%','fontSize':24,'float':'left'})
        ])
        ])

@app.callback(
    Output('feature-graphic4', 'figure'),
    [Input('mu', 'value')])
def update_graph4(mu):
    x = list(range(int(2.6*mu)))
    y = [poisson.pmf(i,mu) for i in range(int(2.6*mu))]
    return {
        'data': [go.Bar(
            x=x,
            y=y,
            width=[0.2]*(int(2.6*mu)),
        )],
        'layout': go.Layout(
            title='Poisson Distribution',
            margin={'l':40, 'b':40, 't':50, 'r':0}
        )
    }

if __name__ == '__main__':
    app.run_server()
