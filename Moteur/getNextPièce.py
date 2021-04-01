echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]

def getNextPiece(coordonées_de_pièce, direction_a_analyser):
    piece_proche = ()
    x = coordonées_de_pièce[0]
    y = coordonées_de_pièce[1]

    while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pièce la plus proche n'est pas trouvé et que le bord du plateau n'est pas atteint, faire :
        piecel=(x,y)
        x += direction_a_analyser[0]
        y += direction_a_analyser[1]
        
        if not (x > 7 or y > 7 or x < 0 or y < 0):
            if echiquier[0][x][y] != []:
                piece_proche = (x,y)
                print("pièce la plus proche enregistré")
        else:
            piece_proche=piecel
            print("mur rencontré")
    return piece_proche

print(getNextPiece((2,0), (0,1)))