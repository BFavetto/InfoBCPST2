# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 23:25:37 2014

@author: Benjamin
"""

def factrec(n):
    assert(n>=0 and type(n)==int)
    if n == 0:
        return 1
    else:
        return n*factrec(n-1)

