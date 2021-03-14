import pygame
from x_coordonnees import *
#marge droite/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
tour_blanche_cn = pygame.image.load("imgs/tour_blanc(cn).png")
tour_blanche_cb = pygame.image.load("imgs/tour_blanc(cb).png")
tour_noir_cn = pygame.image.load("imgs/tour_noir(cn).png")
tour_noir_cb = pygame.image.load("imgs/tour_noir(cb).png")

tour_blanche_cn = pygame.transform.scale(tour_blanche_cn,(31,31))
tour_blanche_cb = pygame.transform.scale(tour_blanche_cb,(31,31))
tour_noir_cn = pygame.transform.scale(tour_noir_cn,(31,31))
tour_noir_cb = pygame.transform.scale(tour_noir_cb,(31,31))

pos_tour_blanche1 = (H,1)
pos_tour_blanche2 = (H,8)
pos_tour_noir1 = (A,8)
pos_tour_noir2 = (A,1)
  
