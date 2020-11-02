# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 13:54:52 2014

@author: Benjamin
"""


def echange(L,i,j):
    L[i],L[j] = L[j],L[i]
    return None
    
def partition(L,gauche,droite):
    """ Partitionne la liste et renvoie la position du pivot"""
    j=gauche+1 # j contient la position courante du debut de la partie > pivot
    for k in range(gauche+1,droite+1):
        if L[k]<=L[gauche]: #si on trouve un element <= pivot
            echange(L,k,j) # on le place en debut de liste
            j=j+1 # mise a jourdu debut de la partie > pivot
    echange(L,gauche,j-1)
    return (j-1)

def quicksort(L,gauche,droite):
    if gauche<droite:
        pivot=partition(L,gauche,droite)
        quicksort(L,gauche,pivot-1)
        quicksort(L,pivot+1,droite)
    return None
    