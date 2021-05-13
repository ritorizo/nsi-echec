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
   
    def coupValide(self, mouvement):
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
   
            # Vérifie que le joueur n'ésaye pas de manger sa propre piéce.
            elif (self.echiquier[x2][y2][1] == self.couleurTour()):
                result = False
				
            # Vérifique que la piéce ne reste pas sur place.
            elif ( (x1 == x2) and (y1 == y2) ):
                result = False 

	# Fait les vérifications spécifiques aux piéces 
	piece = self.echiquier[0][x1][y1][0]
        if (result == True):
			
		# Verif roi <fait>
		if (piece == 'K'): 
			if (4 < ((x1-x2)**2+(y1-y2)**2)):
				result = False
		
		# Verif reinne <fait>
		elif (piece == 'Q'):
                        delta = ((x2-x1), (y2-y1))
                        dirrection = (signe(delta[0]), signe(delta[1]))
                        nextpiece = getNextPiece((x1, y1), dirrection)
                        deltaMax = ((nextpice[0]-x1), nextpiece[1]-y1 )

                        if (abs(delta[0] > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                                result == False
			
		# Verif fou <fait>
		elif (piece == 'F'):
                    if (estDiagonale(mouvement)):
                        delta = ((x2-x1), (y2-y1))
                        dirrection = (signe(delta[0]), signe(delta[1]))
                        nextpiece = getNextPiece((x1, y1), dirrection)
                        deltaMax = ((nextpice[0]-x1), nextpiece[1]-y1 )

                        if (abs(delta[0] > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                                result == False
                    else :
                        result = False
							
		# Verif cavalier <fait>
		elif (piece == 'C'):
			if !(( (x1-x2)**2 + (y1-y2)**2 ) == 13 ): 
				result = False
			
		#Verif tour <fait>
		elif (piece == 'T'):
                    if (estDroit(mouvement)):
                        delta = ((x2-x1), (y2-y1))
                        dirrection = (signe(delta[0]), signe(delta[1]))
                        nextpiece = getNextPiece((x1, y1), dirrection)
                        deltaMax = ((nextpice[0]-x1), nextpiece[1]-y1 )

                        if (abs(delta[0] > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                                result == False
                    else :
                        result = False
							
		
		# Verif pion <fait>
		elif (piece == 'P'):
			# Vérifie le sens du plateau
			facteurSens = 1
			if (self.couleurTour == 'N'):
				facteurSens = -1
				
			mouv = ((x1-x2), (y1-y2)*facteurSens)
			
			if ( ( mouv == (0, 1) ) && ( self.echiquier[x2][y2][0] == "" ) ):
                        elif ( (abs(mouv[0]), mouv[1]) == (1, 1) && ( self.echiquier[0][x2][y2] != "" ) ): # Si (le mouvement va en diagonale et va dans le bon sens) && La case de destination contien une piéce.
                        elif (mouv == (0, 2) && (y1 == (3.5+(2.5)*facteurSens)) && (self.echiquier[x2][y2][0] != "")  ):
                        elif ( (abs(mouv[0]), mouv[1]) == (1, 0) && ( self.echiquier[0][x2][y2][0] == 'P'):  
                        else :
                            result=False
				
                tmp = self.echiquier
                tmp[0][x2][y2] = tmp[0][x1][y1]
                tmp[0][x1][y1] = ""

                if (result && (echequrAuRoi(couleurTour(), echiquier))):
                    result = False
			
        return result
	  

def estDiagonale(mouv): 
    result = False
    if ( abs((mouv[0][0]-mouv[1][0])/(mouv[0][1]-mouv[1][1])) == 0.5 ): # Si (x1-x2)/(y1-y2) == 0.5
        result = True

    return result


def estDroit(mouv):
    result = False
    if ( ((mouv[0][0] - mouv[1][0]) * (mouv[0][1] - mouv[1][1])) == 0): # Si ((x1 - x2) * (y1 - y2)) == 0
        result = True

    return result


def signe(x):
    if (x == 0):
        return 0
    else: 
        return ( x/abs(x) )

def couleur(echiquier)
    retour = "N"
    if ((echiquier[1] % 2) == 0)
        retour = "B"
    return retour
