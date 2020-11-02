# -*- coding: utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt

# simulation d'une variable aléatoire prenant les valeurs x0 , ... , xn
# avec probabilités p0, ... , pn

def simugen(P,X):
    assert(len(P)==len(X))
    F=np.cumsum(P)
    r = random.random()
    k=0
    while r > F[k] :
        k=k+1
    return X[k]
    
N=1000 # 1000 simulations
test=[0.3, 0.2, 0.4, 0.1]
val=[1,2,4,5]
X=[simugen(test,val) for k in range(N)]

n=max(X)
    
bins=np.linspace(1,n,n)
plt.bar(bins,[0.3,0.2,0,0.4,0.1],color='r',width=0.2)

bins2=np.linspace(1,n+1,n+1)
(histo,cl)=np.histogram(X,bins2) #utilisation de la fonction histogram 

plt.bar(bins+0.2,histo/N,color='b',width=0.2) #superposition des deux diagrammes
plt.show()
    