# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 00:16:30 2014

@author: Benjamin
"""

import math

eps = float(input("entrer epsilon:"))
n=math.floor(1/eps)+1

S=0.
for k in range(1,n+1):
    S=S+1./(k**2)

print(S)