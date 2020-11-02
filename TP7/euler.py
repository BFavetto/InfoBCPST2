# -*- coding: utf-8 -*-


import math
import numpy as np
import matplotlib.pyplot as plt

def euler(F,a,b,y0,h):
    y=y0
    t=a
    liste_y = [y0]
    liste_t = [a]
    while t+h <=b:
        y = y+ h*F(t,y)
        t = t+h
        liste_y.append(y)
        liste_t.append(t)
    return (liste_t,liste_y)

# euler(lambda t,y : y,0,1,1,1/100)

# méthode d'euler pour les equations scalaires

def eulerbis(F,y0,T,N):
    h = T/N
    X = np.linspace(0,T,N+1) # attention : N intervalles, N+1 points
    Y = np.zeros(N+1)
    Y[0] = y0
    for k in range(N):
        Y[k+1] = Y[k] + h*F(X[k], Y[k])
    return (X,Y)

F1 = lambda t,y : -y

t0 = 0
y0 = 1
T = 1

for k in range(1,10):
    X,Y = eulerbis(F1, y0, T, 10*k)
    plt.plot(X,Y, color='black')

Z = np.exp(-X)
plt.plot(X,Z,color='red')
plt.show()
#plt.close()


F2 = lambda t,y : y

t0 = 0
y0 = 1
T = 5

for k in range(1,10):
    X,Y = eulerbis(F2, y0, T, 10*k)
    plt.plot(X,Y, color='black')

Z = np.exp(X)
plt.plot(X,Z,color='red')
plt.show()



