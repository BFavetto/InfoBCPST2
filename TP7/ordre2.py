# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 13:32:47 2015

@author: Benjamin
"""

import numpy as np # pour les opérations matricielles
import matplotlib.pyplot as plt

# (1,2) + (4,5)
# [1,2] + [4,5]
# t0 = 0

def euler_ordre2(F,y0,yp0,T,N):
    h = T/N
    X = np.linspace(0,T,N+1) # attention : N intervalles, N+1 points
    y = np.array([y0,yp0])
    res_y = [y]
    for k in range(N):
        y = y + h*F(X[k], y)
        res_y.append(y)
    return (X,res_y)
    
T=3*np.pi

F1 = lambda t,y : np.array([y[1],-y[0]])

y0 = 0
yp0 = 1

X,Y = euler_ordre2(F1,y0,yp0,T,100)

Z=np.array(Y)[:,0] # transformation de la liste des valeurs de y

plt.figure()
plt.grid()
plt.plot(X,Z,color='red')
plt.show()
    
