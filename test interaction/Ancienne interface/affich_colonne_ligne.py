import pygame
from generation_par_tableau import *
pygame.init()
def colonne_ligne() :
  ecran_x = 500
  ecran_y = 248 # 126
  taille_ecran = (ecran_x,ecran_y)
  marge = (ecran_x-ecran_y)/2
  taille_case = int(ecran_y/9)
  marge_gauche = marge + taille_case
  marge_haut = taille_case
  ecran = pygame.display.set_mode(taille_ecran)
  police = pygame.font.Font(None,taille_case+10)
  Colonne = ["A","B","C","D","E","F","G","H"]
  Ligne = ["1","2","3","4","5","6","7","8"]
  for x in range(8) :
    lettre = police.render(Colonne[x],True,pygame.Color("#FFFFFF"))
    chiffre = police.render(Ligne[x],True,pygame.Color("#FFFFFF"))
    ecran.blit(lettre,[marge,(x*taille_case)+marge_haut+4])
    ecran.blit(chiffre,[marge_gauche+(x*taille_case)+10,0])
