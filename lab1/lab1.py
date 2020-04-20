import numpy

from scipy.integrate import quad
from scipy.interpolate import splrep, splev, lagrange
from numpy import exp

DELTA = 0.0000000001

def f(x):
    return 1 - exp(-x)

def F(x, c):
    return x + exp(-x) + c

def spline_func(x):
    array_of_x,  array_of_y = make_arrays(0, 3, 0.3)
    spline_coefficients = splrep(array_of_x, array_of_y)
    return splev(x, spline_coefficients)

def make_arrays(x0, x1, h):
    array_of_x = numpy.arange(x0, x1 + DELTA, h)
    array_of_y = numpy.array([f(xk) for xk in array_of_x])
    return array_of_x, array_of_y


array_of_x,  array_of_y = make_arrays(0, 3, 0.3)

polynom = lagrange(array_of_x, array_of_y)
print('Integral of f(x): ' + str(F(3, 0) - F(0, 0)))
y, _ = quad(spline_func, 0, 3)
print('Integral of spline: ' + str(y))
y, _ = quad(polynom, 0, 3)
print('Integral of polynom: ' + str(y)) 
