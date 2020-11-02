# -*- coding: utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt

def geometrique(p):
    X=1
    while random.random()>p:
        X=X+1
    return(X)

def geoinv(p):
    return(math.ceil(math.log(1-random.random())/math.log(1-p)))
    
N=1000 # 1000 simulations
p=0.4
X=[geometrique(p) for k in range(N)]

n=max(X)
P=np.zeros(n+1)
for k in range(1,n+1):
    P[k]=p*(1-p)**(k-1) # tableau des probabilités
    
bins=np.linspace(0,n,n+1)
plt.bar(bins,P,color='r',width=0.2)

bins2=np.linspace(0,n+1,n+2)
(histo,cl)=np.histogram(X,bins2) #utilisation de la fonction histogram 

plt.bar(bins+0.2,histo/N,color='b',width=0.2) #superposition des deux diagrammes
plt.show()

