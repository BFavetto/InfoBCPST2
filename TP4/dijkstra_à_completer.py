# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:36:40 2014

@author: Benjamin
"""

import numpy as np

G=np.array([[0,3,1,Inf,Inf,Inf],[3,0,1,2,Inf,Inf],[1,1,0,3,5,Inf],[Inf,2,3,0,1,3],[Inf,Inf,5,1,0,1],[Inf,Inf,Inf,3,1,0]])

def dijkstra(G,depart,arrivee):
    N =np.size(G,0) 

    parcours=list() 
    for i in range(N):
        parcours.append([Inf,None,False]) 


    ville_select=  
    dist_interm=


    while 
        minimum=
        for k in range(N):
            if parcours[k][2]==
                dist=
                dist_totale=
                if dist != 0 and dist_totale < parcours[k][0]:
                    parcours[k][0]=
                    parcours[k][1]=
                if parcours[k][0]<minimum:
                    minimum=
                    prochaine_ville_select=k 
        ville_select=prochaine_ville_select 
        parcours[ville_select][2]=
        dist_interm=
        
    chemin=list() 
    ville=
    chemin.append(ville)
    while ville !=
        ville=
        chemin.append(ville)
            
    return



