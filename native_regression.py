import matplotlib.pyplot as plt
from matrix import *

def regression():
    loaded = loadtxt('chirps-modified.txt')
    loadedTransposed=transpose(loaded)
    X=loadedTransposed[0]
    Y=loadedTransposed[1]

    Xp= powers(X,0,1)
    Yp= powers(Y,1,1)
    Xpt=transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    Y2 = [0 for i in range(len(X))]

    for i in range(len(X)):
        Y2[i] = b + m * X[i]

    plt.plot(X, Y, 'ro')
    plt.plot(X, Y2)
    plt.show()


regression()