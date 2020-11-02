# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:05:38 2014

@author: Benjamin
"""


import numpy as np
import matplotlib.pyplot as plt
import math


def suiterec(f,u,n):
    
    x=np.linspace(0,5,200) 
    y=[f(z) for z in x] 
        
    U=np.zeros(n) 
    U[0]=u 
    for k in range(1,n):
        U[k]=f(U[k-1])
        
    Abscisse=np.zeros(2*n)
    Ordonnee=np.zeros(2*n)

    Abscisse[0]=u;
    Ordonnee[0]=u; 
    
    for j in range(1,n):
       Abscisse[2*j]=U[j];Abscisse[2*j-1]=U[j-1]
       Ordonnee[2*j]=U[j];Ordonnee[2*j-1]=U[j]

    Abscisse[2*n-1]=U[n-1]    
    Ordonnee[2*n-1]=f(U[n-1])
    
    return (x,y,Abscisse,Ordonnee,U)
    
u=2.0
n=10
    
(x,y,Abs,Ord,U)=suiterec(math.sin,u,n)

plt.plot(x,y,'b-',x,x,'k-',Abs[1:],Ord[1:],'red',label='$u_{n+1}=f(u_n)$')
plt.ylim(ymin = 0.)
plt.xlabel('$u_n$')
plt.ylabel('$f(u_n)$')
plt.title("suite recurrente")

plt.savefig("suite_rec.png")
plt.show()    
    
