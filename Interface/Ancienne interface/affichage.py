import pygame
from position_tour import *
from x_coordonnees import *
from position_cav import *
from position_fou import *
from position_reine import *
from position_roi import *
from position_pion import *
from generation import *
from generation_par_tableau import *
from affich_colonne_ligne import *
from case_input import *


def affichage() :
  #generation()
  generation_par_tableau()
  
  pygame.display.flip()
  
  
  # Stopper le programme si la fenêtre est fermé.
  for event in pygame.event.get():
    if event.type == pygame.QUIT : 
      running = False
      pygame.quit()
      print("Fermeture")