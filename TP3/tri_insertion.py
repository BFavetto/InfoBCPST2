# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 00:06:05 2014

@author: Benjamin
"""
    
def tri_insertion(L):
    n=len(L)
    for i in range(n):
        x=L[i]
        j=i
        while (j>0 and L[j-1]>x):
            L[j] = L[j-1]
            j=j-1
        L[j]=x
    return L