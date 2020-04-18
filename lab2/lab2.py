import numpy

A = numpy.asmatrix([[13.0, 2.0, 8.0, -7.0, 7.0, 5.0, -7.0, -7.0],
                   [7.0, 2.0, -4.0, 2.0, 3.0, 3.0, -1.0, -2.0],
                   [-7.0, 2.0, 1.0, 3.0, 6.0, -6.0, -3.0, -4.0],
                   [-2.0, -8.0, -6.0, -1.0, 6.0, 2.0, 1.0, -4.0],
                   [0.0, 4.0, -7.0, 1.0, 22.0, 0.0, -6.0, -6.0],
                   [0.0, -3.0, -6.0, 6.0, 4.0, 13.0, 0.0, 6.0],
                   [-8.0, -6.0, -4.0, 7.0, -5.0, -5.0, -2.0, 1.0],
                   [5.0, 5.0, -2.0, -2.0, -3.0, 0.0, -7.0, 14.0]])

B = numpy.asmatrix([[6.0],[36.0],[-25.0],[-57.0],[32.0],[62.0],[-71.0],[70.0]])

P = [1.0, 0.1, 0.01, 0.0001, 0.000001]

def newMatrixes(A, B, p):
    A[0, 0] = 13.0 + p
    B[0, 0] = 6.0 + 4 * p
    newA = A.transpose() * A
    newB = A.transpose() * B
    return newA, newB

def printAll(newA, newB, X, newX, delta, p):
    print('P = ', p)
    print("A(0,0):\t" + format(A[0, 0]))
    print("B(0,0):\t" + format(B[0, 0]))
    print("X = " + format(X))
    print("newX = " + format(newX))
    print("COND = " + format(numpy.linalg.cond(A)) + "\n")
    print("delta = || x - newx || / || x || = " + format(delta))
    print("\n\n\n")

for p in P:
    newA, newB = newMatrixes(A, B, p)
    X = numpy.linalg.solve(A, B)   
    newX = numpy.linalg.solve(newA, newB)
    delta = numpy.linalg.norm(X - newX) / numpy.linalg.norm(X)
    printAll(newA,newB, X, newX, delta, p)
    
