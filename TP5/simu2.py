# -*- coding: utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt

def uniforme(a,b):
    return(a+math.floor(random.random()*((b-a)+1)))

# Tracé d'un diagramme en batons pour comparer les probabilités (théorique)
# et les frequences (issues des simulations)

N=1000 # 1000 simulations
n=4 # loi uniforme sur [[1,4]]
X=[uniforme(1,n) for k in range(N)]

P=np.zeros(n)
for k in range(n):
    P[k]=1/n # tableau des probabilités
    
bins=np.linspace(1,n,n)
plt.bar(bins,P,color='r',width=0.2)

bins2=np.linspace(1,n+1,n+1)
(histo,cl)=np.histogram(X,bins2) #utilisation de la fonction histogram 

plt.bar(bins+0.2,histo/N,color='b',width=0.2) #superposition des deux diagrammes
plt.show()


    