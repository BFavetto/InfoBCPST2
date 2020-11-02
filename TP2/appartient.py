# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:50:58 2014

@author: Benjamin
"""

def appartient(x,L):
    i=0
    while i < len(L) and L[i] != x:
        i+=1
    return i < len(L)
    
def appartient2(x,L):
    for y in L:
        if y==x:
            return True
    return False

def indice(x,L):
   for i,y in enumerate(L):
       if y ==x:
           return i
        
   return None
