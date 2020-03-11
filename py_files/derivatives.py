import numpy as np

def find_term_derivative(term):
    constant = term[0]*term[1]
    exponent = term[1] - 1
    return (constant, exponent)

def find_derivative(function_terms):
    derivative_terms = list(map(lambda term: find_term_derivative(term),function_terms))
    return list(filter(lambda derivative_term: derivative_term[0] != 0, derivative_terms))
def term_output(term, input_value):
    return term[0]*input_value**term[1]

def output_at(list_of_terms, x_value):
    outputs = list(map(lambda term: term_output(term, x_value), list_of_terms))
    return sum(outputs)

def derivative_at(terms, x):
    derivative_fn = find_derivative(terms)
    total = 0
    for term in derivative_fn:
        total += term[0]*x**term[1]
    return total