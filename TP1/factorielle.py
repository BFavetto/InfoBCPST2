# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 13:29:27 2014

@author: Benjamin
"""

def factorielle(n):
    """ calcule n! """
    fact=1

    for k in range(n):
        fact=(k+1)*fact
    
    return fact