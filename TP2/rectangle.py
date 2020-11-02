# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:55:42 2014

@author: Benjamin
"""

import math

def rectangle(f,a,b,n):
    S=0.
    for k in range(n):
        S=S+f(a+k*(b-a)/n)
    S=S*(b-a)/n
    return S
    

eps=float(input("entrer epsilon:"))  

def g(x):
    return 1/(1+x)
    
N=math.floor(1/(2*eps)) +1
print(rectangle(g,0,1,N))
