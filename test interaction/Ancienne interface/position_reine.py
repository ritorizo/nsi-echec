import pygame
from x_coordonnees import *
#marge droite/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
reine_blanche_cn = pygame.image.load("imgs/reine_blanc(cn).png")
reine_blanche_cb = pygame.image.load("imgs/reine_blanc(cb).png")
reine_noir_cn = pygame.image.load("imgs/reine_noir(cn).png")
reine_noir_cb = pygame.image.load("imgs/reine_noir(cb).png")

reine_blanche_cn = pygame.transform.scale(reine_blanche_cn,(31,31))
reine_blanche_cb = pygame.transform.scale(reine_blanche_cb,(31,31))
reine_noir_cn = pygame.transform.scale(reine_noir_cn,(31,31))
reine_noir_cb = pygame.transform.scale(reine_noir_cb,(31,31))

pos_reine_blanche1 = (H,4)
pos_reine_noir1 = (A,4)



  
