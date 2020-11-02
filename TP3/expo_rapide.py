# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 14:23:11 2014

@author: Benjamin
"""

def expo_rapide(n):
    assert (n >= 0 and type(n)==int)
    if n==0:
        return 1
    else:
        r=expo_rapide(n//2)
        if n%2 == 0:
            return r*r
        else:
            return 2*r*r
    
