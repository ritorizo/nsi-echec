import pygame
from x_coordonnees import *
#marge droite/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
fou_blanche_cn = pygame.image.load("imgs/fou_blanc(cn).png")
fou_blanche_cb = pygame.image.load("imgs/fou_blanc(cb).png")
fou_noir_cn = pygame.image.load("imgs/fou_noir(cn).png")
fou_noir_cb = pygame.image.load("imgs/fou_noir(cb).png")

fou_blanche_cn = pygame.transform.scale(fou_blanche_cn,(31,31))
fou_blanche_cb = pygame.transform.scale(fou_blanche_cb,(31,31))
fou_noir_cn = pygame.transform.scale(fou_noir_cn,(31,31))
fou_noir_cb = pygame.transform.scale(fou_noir_cb,(31,31))

pos_fou_blanche1 = (H,3)
pos_fou_blanche2 = (H,6)
pos_fou_noir1 = (A,6)
pos_fou_noir2 = (A,3)


  
