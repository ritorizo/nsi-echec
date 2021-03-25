import pygame
from x_coordonnees import *
#marge dpionte/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
pion_blanc_cn = pygame.image.load("imgs/pion_blanc(cn).png")
pion_blanc_cb = pygame.image.load("imgs/pion_blanc(cb).png")
pion_noir_cn = pygame.image.load("imgs/pion_noir(cn).png")
pion_noir_cb = pygame.image.load("imgs/pion_noir(cb).png")

pion_blanc_cn = pygame.transform.scale(pion_blanc_cn,(31,31))
pion_blanc_cb = pygame.transform.scale(pion_blanc_cb,(31,31))
pion_noir_cn = pygame.transform.scale(pion_noir_cn,(31,31))
pion_noir_cb = pygame.transform.scale(pion_noir_cb,(31,31))

pos_pion_blanche1 = (G,1)
pos_pion_blanche2 = (G,2)
pos_pion_blanche3 = (G,3)
pos_pion_blanche4 = (G,4)
pos_pion_blanche5 = (G,5)
pos_pion_blanche6 = (G,6)
pos_pion_blanche7 = (G,7)
pos_pion_blanche8 = (G,8)

pos_pion_noir1 = (B,1)
pos_pion_noir2 = (B,2)
pos_pion_noir3 = (B,3)
pos_pion_noir4 = (B,4)
pos_pion_noir5 = (B,5)
pos_pion_noir6 = (B,6)
pos_pion_noir7 = (B,7)
pos_pion_noir8 = (B,8)





  
