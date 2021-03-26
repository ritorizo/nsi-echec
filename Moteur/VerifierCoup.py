from Sauvegarde import sauvegarde

echiquier = [[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], 0]

def gestion_coup_valider(mouvement): # mouvement entrée sous la forme ((0,5),(1,6))
    
    sauvegarde(echiquier)

    echiquier[mouvement[1][0]] = echiquier[mouvement[0][0]] # déplacement du pion avec les coordonées entré par mouvement. (sur les trois prochaines lignes)
    echiquier[mouvement[1][1]] = echiquier[mouvement[0][1]]
    echiquier[mouvement[0][0]] = [] 
    
    echiquier[-1]+=1 # on ajoute 1 au compteur de tour.

    return echiquier

gestion_coup_valider(((0,0),(0,1)))