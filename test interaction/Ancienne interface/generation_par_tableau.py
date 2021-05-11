import pygame
from position_tour import *
from x_coordonnees import *
from position_cav import *
from position_fou import *
from position_reine import *
from position_roi import *
from position_pion import *
from carre_vide import *
from echiquier_tableau import *
from test_déplacement_pion import *
from affich_colonne_ligne import *
from case_input import *


def generation_par_tableau() :  
  pygame.init()
  pygame.display.set_caption("test")

  ecran_x = 500
  ecran_y = 248
  taille_ecran = (ecran_x,ecran_y)
  marge = (ecran_x-ecran_y)/2
  taille_case = ecran_y/9
  marge_gauche = marge + taille_case
  marge_haut = taille_case

  screen = pygame.display.set_mode(taille_ecran)

  gene_fini = False
  generation_case_vide = False
  x_vide = marge
  y_vide = taille_case*2
  couleur_case = True # Blanc

  
  changer = True
  
  running = True
  while running == True :
    colonne_ligne()
    input()
    while changer == True :
      #cgt_pion()
      for x in range(8) :
        for y in range(8) :
          if echiquier[x][y] == "tour_noir" :
            if couleur_case == True :
              screen.blit(tour_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(tour_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True

          if echiquier[x][y] == "cav_noir" :
            if couleur_case == True :
              screen.blit(cav_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(cav_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "fou_noir" :
            if couleur_case == True :
              screen.blit(fou_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(fou_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "reine_noir" :
            if couleur_case == True :
              screen.blit(reine_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(reine_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "vide" :
            if couleur_case == True :
              screen.blit(cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "roi_noir" :
            if couleur_case == True :
              screen.blit(roi_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(roi_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "pion_noir" :
            if couleur_case == True :
              screen.blit(pion_noir_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(pion_noir_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "pion_blanc" :
            if couleur_case == True :
              screen.blit(pion_blanc_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(pion_blanc_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "tour_blanc" :
            if couleur_case == True :
              screen.blit(tour_blanche_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(tour_blanche_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "cav_blanc" :
            if couleur_case == True :
              screen.blit(cav_blanche_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(cav_blanche_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "fou_blanc" :
            if couleur_case == True :
              screen.blit(fou_blanche_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(fou_blanche_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "roi_blanc" :
            if couleur_case == True :
              screen.blit(roi_blanche_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(roi_blanche_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if echiquier[x][y] == "reine_blanc" :
            if couleur_case == True :
              screen.blit(reine_blanche_cb,((y*taille_case)+marge_gauche,x*taille_case+marge_haut))
              couleur_case = False
            else :
              screen.blit(reine_blanche_cn,((y*taille_case)+marge_gauche,(x*taille_case+marge_haut)))
              couleur_case = True
          if y == 7:
            if couleur_case == True :
              couleur_case = False
            else :
              couleur_case = True
            
      changer = False

      pygame.display.flip()


      
    
  
  
  