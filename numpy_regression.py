import matplotlib.pyplot as plt
from numpy import *
import sys

def regression():
    cur_dir = sys.argv[1] if len(sys.argv) > 1 else 'dataset3.txt'
    n = sys.argv[2] if len(sys.argv) > 2 else 4
    n=int(n) #Löste kanske error jag fick från python terminal?
    # får inte error längre i alla fall
    #print(n)
    loaded=loadtxt(cur_dir)
    loadedTransposed=transpose(loaded)
    X=loadedTransposed[0]
    Y=loadedTransposed[1]

    Xp= powers(X,0,n)
    Yp= powers(Y,1,1)
    Xpt = Xp.transpose()


    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[:, 0]

    start = int(X[0])
    end = int(X[-1])
    n=int((end-start)/(0.2))

    X2=linspace(start, end, n).tolist()
    X2=array(X2)


    Y2 = [0 for i in range(len(X2))]
    for i in range(len(X2)):
        Y2[i] += poly(a,(X2[i]))

    Y2=array(Y2)

    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()

def poly(a,x):
    value=0
    for i in range(len(a)):
        value += a[i]*x**(i)
    return value


def powers(list,a,b):
    powersMatrix = []
    if len(list) == 0:
        return array(powersMatrix)
    elif a==b > 0:
        powersMatrix = [[0 for i in range(a,b+1)]  # fyller med rows med 0
                            for j in range(len(list))]  # fyller kolumner med 0
        for i in range(a,b+1):
            for j in range(len(list)):
                powersMatrix[j][0]=(list[j]**a)
        return array(powersMatrix)

    elif len(list) == 1:
        powersMatrix = [[0 for i in range(a,b+1)]]

        for i in range(a,b+1):
            powersMatrix[0][i]=(list[0]**i)
        return array(powersMatrix)
    else:
        powersMatrix = [[0 for i in range(a,b+1)]  # fyller med rows med 0
                            for j in range(len(list))]  # fyller kolumner med 0
        for i in range(a,b+1):
            for j in range(len(list)):
                powersMatrix[j][i]=(list[j]**i)
        return array(powersMatrix)

regression()
