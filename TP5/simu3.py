# -*- coding: utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt

def bernoulli(p):
    if random.random()<p:
        return(1)
    else:
        return(0)

# simulation d'une loi binomiale (nombre de succes parmi n repetitions independantes)

def binomiale(n,p):
    X=0
    for k in range(0,n):
        X=X+bernoulli(p)
    return(X)
    
# np.random.binomial(10,0.3)
    
N=5000 # nombre de simulations
n=50 
p=0.5
X=[np.random.binomial(n,p) for k in range(N)]

bins=np.linspace(0,n+1,n+2)
(histo,cl)=np.histogram(X,bins) #utilisation de la fonction histogram 
plt.hist(X,bins,normed=True)
#plt.bar(bins,histo/N,color='b',width=0.2) #superposition des deux diagrammes
#plt.show()    
    
    
# illustration de la convergence vers la loi de Poisson avec lambda =1

N=15 # On a P(X>N) proche de 0

P=[math.exp(-1)/math.factorial(k) for k in range(N+1)]
    
bins=np.linspace(0,N,N+1)
plt.bar(bins,P,color='r',width=0.2)

n=50

B50 = [math.factorial(n)/(math.factorial(k)*math.factorial(n-k))*(1/n**k)*(1-1/n)**(n-k) for k in range(N+1)]

bins2=np.linspace(0,N,N+1)
plt.bar(bins+0.2,B50,color='b',width=0.2) 

n=200

B200 = [math.factorial(n)/(math.factorial(k)*math.factorial(n-k))*(1/n**k)*(1-1/n)**(n-k) for k in range(N+1)]

bins3=np.linspace(0,N,N+1)
plt.bar(bins3+0.4,B200,color='y',width=0.2)

plt.show()