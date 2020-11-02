# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:37:04 2014

@author: Benjamin
"""

def maxi(L):
    M=L[0]
    rang=[0]
    for k in range(1,len(L)):
        if L[k] > M:
            M=L[k]
            rang=[k]
        elif L[k] == M:
            rang.append(k)
            
    return M,rang