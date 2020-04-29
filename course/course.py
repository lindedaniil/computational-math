#from math import *
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
    #while (abs(a-b) > 1e-5):
     #   c = (a + b) / 2
      #  if f2(a) > f2(c):
     #       a = c
    #    else:
     #       b = c
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
#l1, l2 = 0.00004, 0.000077
print(l1,l2)

xx = []
yy = []
yy2 = []

t = 1000
while (t <= 9000):
    res, err = eff(t, l1, l2)
    print( "t: " + str(t) + "\te: " + str(res) + "\teff: " + str(err) )
    xx.append( t )
    yy.append( res )
    yy2.append( err )
    t = t + 1000

plt.plot(xx, yy)
plt.plot(xx, yy2)
print(xx,'\n',yy,'\n',yy2)
plt.show()