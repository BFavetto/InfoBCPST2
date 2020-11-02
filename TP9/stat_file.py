# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 20:46:10 2015

@author: Benjamin
"""

import sys
import os

os.getcwd() # Récupère le répertoire courant
os.chdir("C:\\Users\\Benjamin\\Documents\\Prépa BCPST2\\Python\\TP11_Estimation_IC_Monte_Carlo")
os.listdir() # Liste le contenu du répertoire courant

#crée une liste vide
notes=[]

# ouvre en lecture le fichier contenant les notes
f=open('notes.txt','r')

#pour chaque ligne (note)
for n in f:
	#ou ajoute la note à la liste
	#on doit explicitement convertir en type float, car n est de type string
	notes.append(float(n))

f.close() #on n'oublie pas de fermer le fichier en fin de lecture

print(notes)

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as sps

S=sps.norm.rvs(loc=0,scale=1,size=1000) 

f=open("doudoulehamster.txt","w")

for x in S:
    f.write(str(x)+'\n')
    
f.close()

sps.norm.ppf(0.975, loc=0, scale=1)