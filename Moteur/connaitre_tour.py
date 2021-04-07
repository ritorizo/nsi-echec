class Moteur:

    echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]


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

moteur = Moteur()
print(moteur.connaitreTour(moteur.echiquier))