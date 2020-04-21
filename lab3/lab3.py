import numpy
from numpy import exp, log, abs
from scipy.integrate import RK45

EPS = 0.0001

x0 = numpy.array([3, -1])

def f(t, x):
    return numpy.array([-130 * x[0] + 900 * x[1] + exp(-10 * t),
                        30 * x[0] - 300 * x[1] + log(1 + 100 * t * t)])
    
def rk3(f, t, oldres, h):
    k1 = h * f(t, oldres)
    k2 = h * f(t + h/2, oldres + k1/2)
    k3 = h * f(t + 3 * h / 4, oldres + 3 * k2 / 4)
    return oldres + (2 * k1 + 3 * k2 + 4 * k3) / 9, t + h

def computingRK3(start, end, step, x0):
    current = start
    res = x0.copy()
    while current < end:
        res, current = rk3(f, current, res.copy(), step)
        print('t = ' + str(round(current, 4)) + ' x1 = ' + str(round(res[0], 4)) 
              + ' x2 = ' + str(round(res[1], 4)))

start = 0.0
end = 0.15
step = 0.0075
res = x0.copy()
current = start
print('--------------------RK45--------------------')
while current < end:
    integrator = RK45(f, current, res.copy(), current + step, EPS)
    while integrator.status == 'running':
        integrator.step()
    res = integrator.y
    current += step
    print('t = ' + str(round(current, 4)) + ' x1 = ' + str(round(res[0], 4)) 
          + ' x2 = ' + str(round(res[1], 4)))
        
    
print('--------------------RK3---------------------')
print(str(step))
computingRK3(start, end, step, x0.copy())      
step = 0.0025
print('\n' + str(step))
computingRK3(start, end, step, x0.copy())


