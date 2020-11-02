# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:58:58 2014

@author: Benjamin
"""

def dichotomie(f,a,b,eps):
    assert f(a)*f(b) <=0 and eps >0
    c,d = a,b
    fc, fd = f(c), f(d)
    while d-c > eps:
        m=(c+d)/2
        fm=f(m)
        if fc*fm <= 0:
            d,fd = m,fm
        else:
            c,fc = m,fm
    return c,d