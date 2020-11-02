# -*- coding: utf-8 -*-



import random
import math
import numpy as np
import matplotlib.pyplot as plt

# loi de Poisson (attention lambda est un mot reserve)

def poisson(mu):
    r=random.random()
    k=0
    p=math.exp(-mu)
    S=p
    while S<r:
        k=k+1
        p=p*mu/k
        S=S+p
    return k
    
# np.random.poisson(3)
    
n=10000
mu=3
X=[poisson(mu) for k in range(n)]
eps=math.sqrt(mu/0.05)

def ic(x,bm,bp):
    if bm<=x and x<=bp :
        return 1
    else :
        return 0

sum(list(map(lambda x: ic(x,mu-eps,mu+eps),X)))



