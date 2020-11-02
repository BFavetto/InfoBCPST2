# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 22:41:41 2015

@author: Benjamin
"""

import math 

def mynewton(f,df,x0,eps):
    u=x0
    v=u -f(u)/df(u)
    while abs(v-u)> eps :
        v,u=(v-f(v)/df(v),v)
    return (u,abs(v-u))
    
# mynewton(lambda x:x**2-2,lambda x:2*x,1,0.001)
# se souvenir que lambda permet de déclarer une fonction en ligne de commande
    
    
#utilisation de la fonction de bibliothèque scipy.optimize
import scipy.optimize
scipy.optimize.newton(lambda x:x**2-2,1)


def mynewtonbis(f,h,x0,eps):
    def approxdf(x):
        return (f(x+h)-f(x-h))/(2*h)
    u=x0
    v=u -f(u)/approxdf(u)
    while abs(v-u)> eps :
        v,u=(v-f(v)/approxdf(v),v)
    return (u,abs(v-u))
    
# mynewtonbis(lambda x:x**2-2,0.0001,1,0.001)
    
    
# exercices de simulation

# on peut représenter l'urne par une liste contenant n zéros puis les entiers 
# de 1 à n
# une autre structure de données est une liste contenant le nombre de chaque boules
# [5,1,1,1,1,1] par exemple au départ pour n=5

from random import randint
import matplotlib.pyplot as plt

def tirage(n):
    U = [0]*n+list(range(1,n+1)) # attention à transformer en liste pour concaténer
    x = randint(0,2*n-1) # tire au hasard une boule
    A = U.pop(x) # enleve la boule de l'urne
    y = randint(0,2*n-2) # tire la seconde boule
    B = U.pop(y)
    if A < B :
        return [B,A]
    else :
        return [A,B]

def plusieurs_tirages(n,m):
    L=[]
    for i in range(m):
        L.append(tirage(n))
    return L
    

def evaluation(n,m):
    somme=0
    for i in range(m):
        T=tirage(n)
        if T[0] == T[1]+1 :
            somme = somme +1
    return somme/m
    

    
    