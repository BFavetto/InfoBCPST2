# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 13:16:26 2014

@author: Benjamin
"""

def hanoi(n,D,I,A):
    assert(n>=1)
    if n==1:
        print(D+"-->"+A)
    else:
        hanoi(n-1,D,A,I)
        print(D+"-->"+A)
        hanoi(n-1,I,D,A)

