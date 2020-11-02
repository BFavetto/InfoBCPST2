# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 00:37:51 2014

@author: Benjamin
"""

import numpy as np

def hilbert(n):
    H=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            H[i,j] = 1/(i+j+1) # attention à l'indexation des tableaux
    return H

# np.linalg.matrix_rank(hilbert(50))