# Listing 2-1. Calculate models based on partial data

import numpy as np
from scipy.optimize import curve_fit

def linear_model(n, a, b):
    return a*n + b

# Sample data
xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

# Coefficients are returned as first argument
[(a,b), _]   = curve_fit(linear_model, np.array(xs), np.array(ys))
print('Linear = {}*N + {}'.format(a, b))

def quadratic_model(n, a, b):
    return a*n*n + b*n

[(a,b), _]   = curve_fit(quadratic_model, np.array(xs), np.array(ys))
print('Quadratic = {:.13f}*N^2 + {}*N'.format(a, b))
