# -*- coding: utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt

# doudou le hamster

A=np.array([[0,0.3,0.5],[0.7,0.4,0.5],[0.3,0.3,0]])

# np.linalg.matrix_power(A,20)

def simugen(P):
    F=np.cumsum(P)
    r = random.random()
    k=0
    while r > F[k] :
        k=k+1
    return k

def simumarkov(X0,M,n):
    X=X0 #etat initial
    for k in range(1,n+1):
        X=simugen(list(M[:,X]))
    return X
    
N=1000 # 1000 trajectoires
n=50 # On simule X50
X=[simumarkov(0,A,n) for k in range(N)]

P=list(np.linalg.matrix_power(A,50)[:,0])
    
bins=np.linspace(0,2,3)
plt.bar(bins,P,color='r',width=0.2)

bins2=np.linspace(0,3,4)
(histo,cl)=np.histogram(X,bins2) #utilisation de la fonction histogram 

plt.bar(bins+0.2,histo/N,color='b',width=0.2) #superposition des deux diagrammes
plt.show()
        