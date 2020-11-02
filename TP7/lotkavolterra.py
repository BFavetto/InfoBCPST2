# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
r = float(input("entrer le coeffcient r"))
p = float(input("entrer le coeffcient p"))
d = float(input("entrer le coeffcient d"))
q = float(input("entrer le coeffcient q"))
proie0 = float(input("nombre de proies initial"))
predat0 = float(input("nombre de predateurs initial"))
T=float(input("temps maximal"))

def F(y,t):
    return(np.array([r*y[0]-p*y[0]*y[1],-d*y[1]+q*y[0]*y[1]]))
    
    
y0=np.array([proie0,predat0])
temps=np.linspace(0,T,501)
res=odeint(F,y0,temps)

plt.figure()
plt.grid()
plt.xlabel("Temps")
plt.ylabel("Effectif")
plt.plot(temps,res[:,0],label="Proie")
plt.plot(temps,res[:,1],label="Predateur")
plt.legend(loc="best")
plt.title("Evolution des populations")

plt.figure()
plt.plot(res[:,0],res[:,1])
plt.title("Portrait de phase")
plt.show()
