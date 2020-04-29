import numpy
from numpy import cos, sqrt,exp, pi
from scipy.integrate import quad
import matplotlib.pyplot as plt

def f(x):
    return cos( pi * x / 2 ) - 2 * sqrt(x)

def solve( a, b ):
    while (abs(a-b) > 1e-5):
        c = (a+b)/2
        if (f(a) * f(c) < 0):
            b = c
        else:
            a = c
    return c

def f2( z ):
    return exp(z) * (2*z*z - 4) + pow(2*z*z-1, 2) + exp(2*z) - 3*pow(z,4)

def min( a, b ):
    phi = 1.0 / ( (1 + sqrt(5)) / 2 )
    while (abs(a-b) > 1e-5):
        x2 = a + (b-a) * phi
        x1 = b - (b-a) * phi
        if (f2(x1) < f2(x2)):
            b = x2
        else:
            a = x1
    return (a+b)/2

def computingLambda():
    y =  solve( 0, 1 )
    l1 = y * 31.66675 * 1e-5
    z = min(-2, -1)
    l2 = -z * 3.039830 * 1e-5
    return l2, l1


def eff(t,l1,l2):
    def under_integr(x):
        return 64.77 / pow(t,4) * (1 / ( pow(x,5) * (exp( 1.432 / (t*x) ) - 1)))
    return quad(under_integr, l1, l2)

l1, l2 = computingLambda()
#l1, l2 = 0.00008, 0.000014
print(l1,l2)

list_of_t = []
list_of_res = []
list_of_err = []

t = 1000
while (t <= 9000):
    res, err = eff(t, l1, l2)
    list_of_t.append( t )
    list_of_res.append( res )
    list_of_err.append( err )
    if t % 1000 == 0:
        print( "t: " + str(t) + "\tres: " + str(res) + "\terr: " + str(err) )
    t = t + 100

plt.plot(list_of_t, list_of_res)
plt.plot(list_of_t, list_of_err)
plt.show()