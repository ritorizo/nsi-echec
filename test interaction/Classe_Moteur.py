class Moteur:

    echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]

    def echecEtMat(self,joueur,mouvement):
        return True

    def connaitreTour(self,echiquier_a_analyser):
        '''
        Permet de savoir à qui est le tour sur l'échiquier.
        ----------
        renvoie "Blanc" si c'est un tour paire.
        renvoie "Noir" si c'est un tour impaire.
        ----------
        Peut être utilisé lors d'un besoin de savoir qui a joué
        '''

        if echiquier_a_analyser[-1] % 2 == 0:
            return "Blanc"
    
        if echiquier_a_analyser[-1] % 2 != 0:
            return "Noir"

    def sauvegarde(self,echiquier_a_sauvegarder):

        sauvegarde_tour = echiquier_a_sauvegarder[-1]
        sauvegarde_tour = str(sauvegarde_tour)
        echiquier_a_sauvegarder = str(echiquier_a_sauvegarder)
        fichier=open('Moteur/logs/sauvegarde_echec.txt','a+')
        fichier.write('Tour ')
        fichier.write(sauvegarde_tour)
        fichier.write(' : ')
        fichier.write(echiquier_a_sauvegarder)
        fichier.write( '\n' )
        fichier.close
        print("Sauvegarde du tour effectué")

    def gestionCoupValider(self,mouvement): # mouvement entrée sous la forme ((0,5),(1,6))

        self.sauvegarde(self.echiquier)
        
        # déplacement du pion avec les coordonées entré par mouvement. (sur les deux prochaines lignes)
        self.echiquier[0][mouvement[1][0]][mouvement[1][1]]=self.echiquier[0][mouvement[0][0]][mouvement[0][1]]
        self.echiquier[0][mouvement[0][0]][mouvement[0][1]]=[]
        
        for x in range(7): # vérifie si un pion va à dame
            if self.echiquier[0][x][0] == ["PN"]:
                self.echiquier[0][x][0] = ["QN"]
            
            if self.echiquier[0][x][7] == ["PB"]:
                self.echiquier[0][x][7] = ["QB"]
        

        if self.echecEtMaths(self.connaitreTour) == True:
            if self.connaitreTour(self.echiquier) == "Blanc":
                self.etat_partie = "Noir a perdu"
            if self.connaitreTour(self.echiquier) == "Noir":
                self.etat_partie = "Blanc a perdu"


        self.echiquier[-1]+= 1 # on ajoute 1 au compteur de tour.


        print("gestionCoupValider effectué")

    def getNextPiece(self,coordonées_de_pièce, direction_a_analyser):
        piece_proche = ()
        x = coordonées_de_pièce[0]
        y = coordonées_de_pièce[1]

        while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pièce la plus proche n'est pas trouvé et que le bord du plateau n'est pas atteint, faire :
            piecel=(x,y)
            x += direction_a_analyser[0]
            y += direction_a_analyser[1]
            
            if not (x > 7 or y > 7 or x < 0 or y < 0):
                if self.echiquier[0][x][y] != []:
                    piece_proche = (x,y)
                    print("pièce la plus proche enregistré")
            else:
                piece_proche=piecel
                print("mur rencontré")
        return piece_proche

    def toutesCasesAvantLaProchainePiece(self,coordonées_de_pièce, direction_a_analyser):
        piece_proche = ()
        x = coordonées_de_pièce[0]
        y = coordonées_de_pièce[1]
        tableau =[]

        while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pièce la plus proche n'est pas trouvé et que le bord du plateau n'est pas atteint, faire :
            x += direction_a_analyser[0]
            y += direction_a_analyser[1]
            piecel=(x,y)
            tableau.append(piecel)


            if not (x > 7 or y > 7 or x < 0 or y < 0):
                if self.echiquier[0][x][y] != []:
                    piece_proche = (x,y)

        if tableau[-1][0] == 8:
            del tableau[-1]
        if tableau[-1][1] == 8:
            del tableau[-1]

        return tableau

moteur = Moteur()
print(moteur.connaitreTour(moteur.echiquier))
moteur.gestionCoupValider(((0,5),(1,5)))