# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 16:14:27 2014

@author: Benjamin
"""

a=int(input("entrer a: "))
b=int(input("entrer b: "))
q=0
r=a
while r>=b:
    q=q+1
    r=r-b
print("q=",q)
print("r=",r)