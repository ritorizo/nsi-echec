import pygame
from x_coordonnees import *
#marge droite/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
cav_blanche_cn = pygame.image.load("imgs/cav_blanc(cn).png")
cav_blanche_cb = pygame.image.load("imgs/cav_blanc(cb).png")
cav_noir_cn = pygame.image.load("imgs/cav_noir(cn).png")
cav_noir_cb = pygame.image.load("imgs/cav_noir(cb).png")

cav_blanche_cn = pygame.transform.scale(cav_blanche_cn,(31,31))
cav_blanche_cb = pygame.transform.scale(cav_blanche_cb,(31,31))
cav_noir_cn = pygame.transform.scale(cav_noir_cn,(31,31))
cav_noir_cb = pygame.transform.scale(cav_noir_cb,(31,31))

pos_cav_blanche1 = (H,7)
pos_cav_blanche2 = (H,2)
pos_cav_noir1 = (A,2)
pos_cav_noir2 = (A,7)
  
