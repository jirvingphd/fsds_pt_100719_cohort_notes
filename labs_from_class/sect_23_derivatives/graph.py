import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
init_notebook_mode(connected=True)

def trace(data, mode = 'markers', name="data"):
    x_values = list(map(lambda point: point['x'],data))
    y_values = list(map(lambda point: point['y'],data))
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name}

def plot_figure(figure):
    plotly.offline.iplot(figure)

def line_function_trace(line_function, x_values, mode = 'line', name = 'line function'):
    values = line_function_data(line_function, x_values)
    values.update({'mode': mode, 'name': name})
    return values

def line_function_data(line_function, x_values):
    y_values = list(map(lambda x: line_function(x), x_values))
    return {'x': x_values, 'y': y_values}

def m_b_data(m, b, x_values):
    y_values = list(map(lambda x: m*x + b, x_values))
    return {'x': x_values, 'y': y_values}

def m_b_trace(m, b, x_values, mode = 'line', name = 'line function'):
    values = m_b_data(m, b, x_values)
    values.update({'mode': mode, 'name': name})
    return values

def plot(traces, layout = {}):
    if not isinstance(traces, list): raise TypeError('first argument must be a list.  Instead is', traces)
    plotly.offline.iplot({'data': traces, 'layout': layout})

def build_layout(x_axis = None, y_axis = None, options = {}):
    layout = {}
    if isinstance(x_axis, dict): layout.update({'xaxis': x_axis})
    if isinstance(y_axis, dict): layout.update({'yaxis': y_axis})
    layout.update(options)
    return layout


def make_subplots(one_one_traces = [], one_two_traces = [], two_one_traces = [], two_two_traces = []):
    if two_one_traces or two_two_traces:
        fig = tools.make_subplots(rows=2, cols=2)
    else:
        fig = tools.make_subplots(rows=1, cols=2)
    for trace in one_one_traces:
        fig.append_trace(trace, 1, 1)
    for trace in one_two_traces:
        fig.append_trace(trace, 1, 2)
    for trace in two_one_traces:
        fig.append_trace(trace, 1, 1)
    for trace in two_two_traces:
        fig.append_trace(trace, 1, 2)
    return fig

def trace_values(x_values, y_values, mode = 'markers', name="data", text = []):
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name, 'text': text}
