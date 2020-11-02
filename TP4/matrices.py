# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 18:09:38 2014

@author: Benjamin
"""

import numpy as np

M=np.array([[1,2,3],[4,5,6]])

D = np.diag([1,2,3])

size(M)

size(M,0)

size(M,1)

np.transpose(M)

np.dot(M,D)

np.linalg.inv(D)

np.linalg.matrix_rank(M)

#matrice Hilbert

from sympy import *
 x = Symbol('x')
 y = Symbol('y')
 solve(x**4 - 1, x)
((x+y)**2).expand()
solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
 apart(1/( (x+2)*(x+1) ), x)

 B = Matrix([[1,2,1],[0,1,2],[1,0,1]])