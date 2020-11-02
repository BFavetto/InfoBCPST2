# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 15:00:47 2015

@author: Benjamin
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd
import scipy.stats as sps

def unif(a,b):
    assert(a <b)
    return a+(b-a)*rd.random()
    
def expo(mu):
    assert(mu>0)
    return -math.log(1-rd.random())/mu
    
    
# densite de la loi expo(1)    
X=np.linspace(0,8,200)

plt.figure()
plt.plot(X,sps.expon.pdf(X,scale=1)) # ATTENTION : scale=1/mu (esperance)
plt.grid()
plt.show()

#fonction de repartition de la loi expo(1)
plt.figure()
plt.plot(X,sps.expon.cdf(X,scale=1))
plt.grid()
plt.show()

def cauchy():
    x=rd.random()
    return math.tan(np.pi*(x-0.5))
    
np.random.exponential(scale=1.0,size=10)

S=sps.expon.rvs(scale=1,size=1000) 

plt.figure()
plt.plot(X,sps.expon.pdf(X,scale=1),color="red")
plt.hist(S,30,normed=True)
plt.show()

sps.norm.ppf(rd.random())

np.random.normal(0,1)
np.random.normal(5,2)

X=np.linspace(-5,5,400)
S=sps.norm.rvs(loc=0,scale=1,size=1000) 

plt.figure()
plt.plot(X,sps.norm.pdf(X,loc=0,scale=1),color="red")
plt.hist(S,20,normed=True)
plt.show()

def normapprox():
    S=0
    for k in range(12):
        S=S+rd.random()
    return S-6
    
X=np.linspace(-5,5,400)
S=[normapprox() for k in range(1000)] 

plt.figure()
plt.plot(X,sps.norm.pdf(X,loc=0,scale=1),color="red")
plt.hist(S,20,normed=True)
plt.show()

N=1000
n=100
p=0.5

Z=np.random.binomial(n,p,N)
Zc=(Z-n*p)/math.sqrt(n*p*(1-p))
plt.figure()
plt.plot(X,sps.norm.pdf(X,loc=0,scale=1),color="red")
plt.hist(Zc,20,normed=True)
plt.show()

