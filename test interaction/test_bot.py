
class mohammed :
    echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["KB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["QB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]
    def toutesCasesAvantLaProchainePiece(self,coordonées_de_pièce, direction_a_analyser):
        piece_proche = ()
        x = coordonées_de_pièce[0]
        y = coordonées_de_pièce[1]
        tableau =[]

        while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pièce la plus proche n'est pas trouvé et que le bord du plateau n'est pas atteint, faire :
            x += direction_a_analyser[0]
            y += direction_a_analyser[1]
            piecel=(x,y)
            tableau.append(piecel)


            if not (x > 7 or y > 7 or x < 0 or y < 0):
                if self.echiquier[0][x][y] != []:
                    piece_proche = (x,y)

        if tableau[-1][0] == 8:
            del tableau[-1]
        if tableau[-1][1] == 8:
            del tableau[-1]

        return tableau

m = mohammed()
print(m.toutesCasesAvantLaProchainePiece((0,0),(0,1)))