echiquier = [[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], 0]

def getNextPiece(coordonées_de_pièce, direction_a_analyser):
    piece_proche = ()
    x = coordonées_de_pièce[0]
    y = coordonées_de_pièce[1]

    while piece_proche == () or x != 7 or y != 7 or x!= 0 or x != 0: # tant que la pièce la plus proche n'est pas trouvé et que le bord du plateau n'est pas atteint, faire :
        echiquier[0][x][y] += echiquier[0][direction_a_analyser[0]][direction_a_analyser[1]]
        # ajouter variable qui permet d'avancer dans la boucle sans toujours faire le m^me mouvement