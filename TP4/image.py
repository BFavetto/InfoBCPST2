# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 20:26:53 2014

@author: Benjamin
"""

# Pour la manipulation des images et des tableaux
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Pour récupérer Léna
import scipy.misc

# Manipulation de fichiers et de répertoires
import os

os.getcwd() # Récupère le répertoire courant
os.chdir("C:\\Users\\Benjamin\\Documents\\Prépa BCPST2\\Python\\TP6_Matrices_Images")
os.listdir() # Liste le contenu du répertoire courant

# image en niveaux de gris
l = scipy.misc.lena() # Image de Léna
plt.gray()
plt.imshow(l)
plt.show()

l.shape # Taille de l'image

# filtrage d'une image en niveaux de gris
def floutage(image):
    (h, l) = image.shape # la taille
    res = image.copy()
    for i in range(1, h−2):
        for j in range(1, l−2):
            voisinage = image[i−1:i+2, j−1:j+2]
            res[i][j] = int(sum(voisinage)/9)
    return(res)

lflou=filtrage(l)
lflou=filtrage(lflou)
plt.gray()
plt.imshow(lflou)
plt.show()

#image en couleurs avec lecture dans un fichier
img = mpimg.imread("chaton.png")
plt.colors()
plt.imshow(img)
plt.show()

img.shape

lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
plt.show()
plt.colorbar()

# plt.hist(img.flatten(), 256, range=(0.0,1.0), fc='k', ec='k')
sauv=img[0:150,0:200,:].copy()
img[0:150,0:200,:]=img[150:,200:,:]
img[150:,200:,:]=sauv
plt.imshow(img)
plt.savefig("chatonbizarre.png")
plt.show()