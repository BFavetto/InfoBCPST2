# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:08:18 2014

@author: Benjamin
"""

import math

x=float(input("entrer x:"))
n=int(input("entrer n:"))

S= 0.

for k in range(n+1):
    S=S+(x**k)/(math.factorial(k))
    
print(S)