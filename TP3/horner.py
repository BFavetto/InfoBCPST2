# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 01:04:24 2014

@author: Benjamin
"""

def horner(P,x):
    assert(P !=[])
    S=0
    for a in reversed(P):
        S = a+x*S
    return S
    