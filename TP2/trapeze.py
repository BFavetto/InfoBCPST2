# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 00:40:19 2014

@author: Benjamin
"""

import math

def g(x):
    return 1/(1+x)
    
def trapeze(f,a,b,n):
    S=(f(a) + f(b))/2.
    for k in range(1,n):
        S= S+f(a+k*(b-a)/n)
    S=S*(b-a)/n
    return S

eps=float(input("entrer epsilon:"))  
    
N=math.floor(1/math.sqrt(6*eps)) +1

print(trapeze(g,0,1,N))
