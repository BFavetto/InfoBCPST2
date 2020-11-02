# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:34:59 2014

@author: Benjamin
"""

def fusion(L1,L2,g,m,d):
    """ fusionne les listes L1[g:m] et L1[m,d] dans la liste L2"""
    i,j =g,m #i parcourt  L1[g:m] et j parcourt L1[m,d]
    for k in range(g,d):
        if i<m and (j==d or L1[i] <=L1[j]):
            L2[k] = L1[i] # on ajoute un élément de L1[g:m] à L2
            i = i+1
        else:
            L2[k] = L1[j] # on ajoute un élément de L1[m:d] à L2
            j = j+1
    return None
    
def tri_fusion(L):
    tmp = L[:] # on recopie la liste pour la modifier 
    def tri_rec(g,d): # fonction recursive locale
        if g >= d-1:
        m=(g+d)//2 # on determine le milieu
        tri_rec(g,m) #on trie recursivement les deux sous-tableaux
        tri_rec(m,d)
        tmp[g:d] = L[g:d]
        fusion(tmp,L,g,m,d) # on effectue la fusion
     return tri_rec(0,len(L))
