# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:23:30 2014

@author: Benjamin
"""

def u(n):
    assert(n>=0)
    if n==0:
        return 1
    elif n==1:
        return 0
    else:
        return u(n-1)+2*u(n-2)


        