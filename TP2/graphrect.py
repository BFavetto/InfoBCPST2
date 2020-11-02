# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 01:23:14 2014

@author: Benjamin
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def g(x):
    return 1/(1+x)

def graphrect(f,a,b,n):
    
    x=np.linspace(a,b,200)
    y=[f(z) for z in x]
    
    Abs=np.zeros(2*n)
    Ord=np.zeros(2*n)
    
    for k in range(n):
        Abs[2*k]=a+(b-a)*k/n
        Abs[2*k+1] = a+(b-a)*(k+1)/n
        Ord[2*k]=f(Abs[2*k])
        Ord[2*k+1]=f(Abs[2*k])        
        
    
    plt.plot(x,y,'b-',Abs,Ord,'red')
    plt.title("Methode des rectangles")
    plt.show()
    return Abs,Ord
    
graphrect(g,0,1,10)


    
    