from Classe_Moteur import *

class Bot:

    def tousCoupsPossible(self, case, echiquier):
        if echiquier[0][case[0]][case[1]] != []:
            if echiquier[0][case[0]][case[1]][0][0] == "F" or "Q":
                # on cherche tous les cases possible sur lequel le fou peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "T" or "Q":
                # on cherche toutes les cases possible sur lequel la tour peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "P":
                # on cherche toutes les cases possible sur lequel le pion peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "K":
                # on cherche toutes les cases possible sur lequel le pion peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "C":
                # on cherche toutes les cases possible sur lequel le cavalier peut aller


    def coupsPossiblePourUneCouleur(self, couleur, echiquier):
        liste_coups = []
        coupsPossibleCouleur = []
        for x in range(8) :
            for y in range(8): 
                    
                pion_candidat = echiquier[0][x][y]
                    
                if pion_candidat != []:
                    if pion_candidat[0][1] == couleur:
                        coupsPossibleCouleur += tousCoupsPossible((x,y), echiquier)
        return coupsPossibleCouleur

