from Sauvegarde import sauvegarde
from connaitre_tour import connaitreTour

class Moteur:

    # la fonction suivante bourre : 

    def EchecEtMat(self,joueur,mouvement):
        return True

    echiquier = [[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], 0] # il s'agit d'un exemple d'échiquier.

    def gestionCoupValider(self,mouvement): # mouvement entrée sous la forme ((0,5),(1,6))

        # sauvegarde(self.echiquier)

        self.echiquier[mouvement[1][0]] = self.echiquier[mouvement[0][0]] # déplacement du pion avec les coordonées entré par mouvement. (sur les trois prochaines lignes)
        self.echiquier[mouvement[1][1]] = self.echiquier[mouvement[0][1]]
        self.echiquier[mouvement[0][0]] = [] 
        
        self.echiquier[-1]+=1 # on ajoute 1 au compteur de tour.

        if EchecEtMaths(self,joueur,mouvement) == True:
            if self.connaitreTour(self,self.echiquier) == "Blanc":
                self.etat_partie = "Noir a perdu"
            if self.connaitreTour(self,self.echiquier) == "Noir":
                self.etat_partie = "Blanc a perdu"


        return self.echiquier

moteur = Moteur()
print(gestionCoupValider(((0,0),(0,1))))