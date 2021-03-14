import pygame
from x_coordonnees import *
#marge droite/gauche echequier : 126
pygame.init()

# Donner un nom à la fenêtre

# x = 1-8, y = 1-8
roi_blanche_cn = pygame.image.load("imgs/roi_blanc(cn).png")
roi_blanche_cb = pygame.image.load("imgs/roi_blanc(cb).png")
roi_noir_cn = pygame.image.load("imgs/roi_noir(cn).png")
roi_noir_cb = pygame.image.load("imgs/roi_noir(cb).png")

roi_blanche_cn = pygame.transform.scale(roi_blanche_cn,(31,31))
roi_blanche_cb = pygame.transform.scale(roi_blanche_cb,(31,31))
roi_noir_cn = pygame.transform.scale(roi_noir_cn,(31,31))
roi_noir_cb = pygame.transform.scale(roi_noir_cb,(31,31))

pos_roi_blanche1 = (H,5)
pos_roi_noir1 = (A,5)



  
