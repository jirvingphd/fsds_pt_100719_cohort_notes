def expected_value_for_line(m, b, x_value):
    return m*x_value + b

def sorted_points(x_values, y_values):
    values = list(zip(x_values, y_values))
    sorted_values = sorted(values, key=lambda value: value[0])
    return sorted_values

def y_intercept(x_values, y_values, m = None):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    if m == None:
        m = slope(x_values, y_values)
    offset = highest[1] - m*highest[0]
    return offset

def slope(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    x1 = sorted_values[0][0]
    y1 = sorted_values[0][1]
    x2 = sorted_values[-1][0]
    y2 = sorted_values[-1][1]
    m = (y2 - y1)/(x2 - x1)
    return m

def build_regression_line(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    lowest = sorted_values[0]
    m = slope(x_values, y_values)
    b = y_intercept(x_values, y_values, m)
    return {'slope': m, 'int': b}
