# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 01:31:41 2014

@author: Benjamin
"""

   
def tri_bulles(L):
    n = len(L)
    echange_ok = False
    while echange_ok == False:
        echange_ok = True
        for j in range(0, n-1):
            if L[j] > L[j+1]:
                echange_ok = False
                L[j],L[j+1] = L[j+1],L[j]
        n = n-1
    return None