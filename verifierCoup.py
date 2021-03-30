# mouvement : ((x1, y1), (x2, y2))
class Moteur:
   
  def couleurTour(self):
       """Cette fonction renvois la couleur du joueur dont c'est le tour
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
   
       for i in (x1, y1, y2, y2):
           if !(0 <= i <= 7)
               result = False
   
       if (result == True)
   
       # Vérifie que le joueur a le droit de séléctioner la piéce qu'il a choisi.
       elif (self.echiquier[x1][y1][1] != self.couleurTour())
           result = False
   
       # Vérifie que le joueur n'essaye pas de manger sa propre piéce.
       elif (self.echiquier[x2][y2][1] == self.couleurTour())
           result = False
   
       # Vérifique que la piéce ne reste pas sur place
       elif ( (x1 == x2) and (y1 == y2) ):
           result = False 
       
       return result 

# Détecte un mouvement diagonale
#if ( abs((x1-x2)/(y1-y2)) == 0.5 ) 
    


# Dit si le mouvement est typique d'un cavalier
#def mouvementCavalier(x1, y1, x2, y2)
#    if (( (x1-x2)**2 + (y1-y2)**2 ) == 13 )


# Dit si un mouvment est droit.
# def mouvementDroit(x1, y1, x2, y2)
#    if ( (x1 == x2) ^ (y2 == y2) ):
#        return True
#    else:
#        return False
