# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 00:20:42 2014

@author: Benjamin
"""

eps=float(input("entrer epsilon:"))

S=1.
n=0

while abs(3./2. -S)>eps:
    S=S+1/3**(n+1)
    n=n+1

print(n)