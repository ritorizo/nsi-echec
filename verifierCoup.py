# mouvement : ((x1, y1), (x2, y2))
class Moteur:
   
    def couleurTour(self):
        """Cette méthdoe renvois la couleur du joueur dont c'est le tour
        ----
        retour : 'N' si le joueur qui joue est noir et 'B' si le joueur qui jou est blanc
        """
        result = 'N'
        if (self.echiquier[1] % 2 == 0)
            result = 'B'
   
        return result
   
    def verifierCoup(self, mouvement):
        x1 = mouvement[0][0]
        y1 = mouvement[0][1]
        x2 = mouvement[1][0]
        y2 = mouvement[1][1]
   
        result = True
   
        # Vérifie que le mouvement ne sort pas de l'échiquier
        for i in (x1, y1, y2, y2):
            if !(0 <= i <= 7)
                result = False
   
        # On fait les vérification générales.
        if (result == True):

            # Vérifie que le joueur a le droit de séléctioner la piéce qu'il a choisi.
            if (self.echiquier[x1][y1][1] != self.couleurTour()):
                result = False
   
)           # Vérifie que le joueur n'ésaye pas de manger sa propre piéce.
            elif (self.echiquier[x2][y2][1] == self.couleurTour()):
                result = False
				
            # Vérifique que la piéce ne reste pas sur place.
            elif ( (x1 == x2) and (y1 == y2) ):
                result = False 

       return result 

def estDiagonale(mouv): 
    result = False
    if ( abs((mouv[0][0]-mouv[1][0])/(mouv[0][1]-mouv[1][1])) == 0.5 ): # Si (x1-x2)/(y1-y2) == 0.5
        result = True

    return result


def estCavlier(mouv):
    result = False
    if (( (mouv[0][0]-mouv[1][0])**2 + (mouv[0][1]-mouv[1][1])**2 ) == 13 ): # Si (x1-x2)**2 + (y1-y2)**2 == 13
        result = True

    return result

def estDroit(mouv):
    result = False
    if ( (mouv[0][0] == mouv[1][0]) ^ (mouv[1][1] == mouv[1][1]) ): # Si (x1 == x2) xor (y1 == y2)
        result = True

    return result
