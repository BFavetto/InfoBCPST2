# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:36:40 2014

@author: Benjamin
"""

import numpy as np

G=np.array([[0,3,1,Inf,Inf,Inf],[3,0,1,2,Inf,Inf],[1,1,0,3,5,Inf],[Inf,2,3,0,1,3],[Inf,Inf,5,1,0,1],[Inf,Inf,Inf,3,1,0]])

def dijkstra(G,depart,arrivee):
    N =np.size(G,0) 

    parcours=list() # la liste mémorise les étapes du parcours du graphe 
    for i in range(N):
        parcours.append([Inf,None,False]) # initialise les distances totales partielles, les antécédents et la nature du sommet


    ville_select=depart 
    dist_interm=0 
#    parcours[depart][0] = 0
#    parcours[depart][2] = True

    while ville_select != arrivee: 
        minimum=Inf
        for k in range(N):
            if parcours[k][2]==False: # si la ville k n'est pas déjà visitée
                dist=G[ville_select][k]
                dist_totale=dist_interm+dist # distance totale en passant par k
                if dist != 0 and dist_totale < parcours[k][0]:
                    parcours[k][0]=dist_totale
                    parcours[k][1]=ville_select
                if parcours[k][0]<minimum:
                    minimum=parcours[k][0]
                    prochaine_ville_select=k # prochaine ville (celle qui minimise la distance partielle)
        ville_select=prochaine_ville_select # numéro de la prochaine ville sélectionnée
        parcours[ville_select][2]=True # la ville est désormais définitive dans le parcours
        dist_interm=parcours[ville_select][0]
        
    chemin=list() # reconstitution du plus court chemin
    ville=arrivee
    chemin.append(ville)
    while ville != depart:
        ville=parcours[ville][1]
        chemin.append(ville)
            
    return(parcours,list(reversed(chemin)))




