from echiquier_tableau import *
def cgt_pion() :
  ancien = input("coordonnées visée")
  nouveau = input("coordonées à aller")
  ancien = list(ancien.split(","))
  nouveau = list(nouveau.split(","))
  save = echiquier[int(ancien[0])][int(ancien[1])]
  echiquier[int(ancien[0])][int(ancien[1])] = echiquier[int(nouveau[0])][int(nouveau[1])]
  echiquier[int(nouveau[0])][int(nouveau[1])] = save
  changer = False