import pygame
from position_tour import *
from x_coordonnees import *
from position_cav import *
from position_fou import *
from position_reine import *
from position_roi import *
from position_pion import *
from carre_vide import *


def generation() :  
  pygame.init()
  pygame.display.set_caption("test")

  ecran_x = 500
  ecran_y = 248
  taille_ecran = (ecran_x,ecran_y)
  marge = (ecran_x-ecran_y)/2
  taille_case = (ecran_x-(marge*2))/8

  screen = pygame.display.set_mode(taille_ecran)

  gene_fini = False
  generation_case_vide = False
  x_vide = marge
  y_vide = taille_case*2
  couleur_case = True # Blanc

  running = True
  while running == True :
  
    while gene_fini == False :
      screen.blit(tour_blanche_cn,(((pos_tour_blanche1[1]-1)*31)+marge,pos_tour_blanche1[0]*31))
      screen.blit(tour_blanche_cb,(((pos_tour_blanche2[1]-1)*31)+marge,pos_tour_blanche2[0]*31))
      screen.blit(tour_noir_cn,(((pos_tour_noir1[1]-1)*31)+marge,pos_tour_noir1[0]*31))
      screen.blit(tour_noir_cb,(((pos_tour_noir2[1]-1)*31)+marge,pos_tour_noir2[0]*31))

      screen.blit(cav_blanche_cn,(((pos_cav_blanche1[1]-1)*31)+marge,pos_cav_blanche1[0]*31))
      screen.blit(cav_blanche_cb,(((pos_cav_blanche2[1]-1)*31)+marge,pos_cav_blanche2[0]*31))
      screen.blit(cav_noir_cn,(((pos_cav_noir1[1]-1)*31)+marge,pos_cav_noir1[0]*31))
      screen.blit(cav_noir_cb,(((pos_cav_noir2[1]-1)*31)+marge,pos_cav_noir2[0]*31))

      screen.blit(fou_blanche_cn,(((pos_fou_blanche1[1]-1)*31)+marge,pos_fou_blanche1[0]*31))
      screen.blit(fou_blanche_cb,(((pos_fou_blanche2[1]-1)*31)+marge,pos_fou_blanche2[0]*31))
      screen.blit(fou_noir_cn,(((pos_fou_noir1[1]-1)*31)+marge,pos_fou_noir1[0]*31))
      screen.blit(fou_noir_cb,(((pos_fou_noir2[1]-1)*31)+marge,pos_fou_noir2[0]*31))

      screen.blit(reine_blanche_cb,(((pos_reine_blanche1[1]-1)*31)+marge,pos_reine_blanche1[0]*31))
      screen.blit(reine_noir_cn,(((pos_reine_noir1[1]-1)*31)+marge,pos_reine_noir1[0]*31))

      screen.blit(roi_blanche_cn,(((pos_roi_blanche1[1]-1)*31)+marge,pos_roi_blanche1[0]*31))
      screen.blit(roi_noir_cb,(((pos_roi_noir1[1]-1)*31)+marge,pos_roi_noir1[0]*31))

      screen.blit(pion_blanche_cb,(((pos_pion_blanche1[1]-1)*31)+marge,pos_pion_blanche1[0]*31))
      screen.blit(pion_blanche_cn,(((pos_pion_blanche2[1]-1)*31)+marge,pos_pion_blanche2[0]*31))
      screen.blit(pion_blanche_cb,(((pos_pion_blanche3[1]-1)*31)+marge,pos_pion_blanche3[0]*31))
      screen.blit(pion_blanche_cn,(((pos_pion_blanche4[1]-1)*31)+marge,pos_pion_blanche4[0]*31))
      screen.blit(pion_blanche_cb,(((pos_pion_blanche5[1]-1)*31)+marge,pos_pion_blanche5[0]*31))
      screen.blit(pion_blanche_cn,(((pos_pion_blanche6[1]-1)*31)+marge,pos_pion_blanche6[0]*31))
      screen.blit(pion_blanche_cb,(((pos_pion_blanche7[1]-1)*31)+marge,pos_pion_blanche7[0]*31))
      screen.blit(pion_blanche_cn,(((pos_pion_blanche8[1]-1)*31)+marge,pos_pion_blanche8[0]*31))

      screen.blit(pion_noir_cn,(((pos_pion_noir1[1]-1)*31)+marge,pos_pion_noir1[0]*31))
      screen.blit(pion_noir_cb,(((pos_pion_noir2[1]-1)*31)+marge,pos_pion_noir2[0]*31))
      screen.blit(pion_noir_cn,(((pos_pion_noir3[1]-1)*31)+marge,pos_pion_noir3[0]*31))
      screen.blit(pion_noir_cb,(((pos_pion_noir4[1]-1)*31)+marge,pos_pion_noir4[0]*31))
      screen.blit(pion_noir_cn,(((pos_pion_noir5[1]-1)*31)+marge,pos_pion_noir5[0]*31))
      screen.blit(pion_noir_cb,(((pos_pion_noir6[1]-1)*31)+marge,pos_pion_noir6[0]*31))
      screen.blit(pion_noir_cn,(((pos_pion_noir7[1]-1)*31)+marge,pos_pion_noir7[0]*31))
      screen.blit(pion_noir_cb,(((pos_pion_noir8[1]-1)*31)+marge,pos_pion_noir8[0]*31))

      while generation_case_vide == False :
        while x_vide != marge+(taille_case*8) :
          if couleur_case == True :
            screen.blit(cb,(x_vide,y_vide))
            couleur_case = False
          else :
            screen.blit(cn,(x_vide,y_vide))
            couleur_case = True
          x_vide+=taille_case
        y_vide+=taille_case
        if y_vide == taille_case*6 and x_vide == marge+(taille_case*8) :
          generation_case_vide = True
        else :
          x_vide = marge
        if couleur_case == True :
          couleur_case = False
        else :
          couleur_case = True


      pygame.display.flip()
    
  
  
  