from connaitre_tour import connaitreTour

echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]

def mise_en_echec(echiquier_a_analyser):
    
    if connaitreTour(echiquier_a_analyser) == "Blanc":
        # chercher le roi blanc sur l'échiquier et renvoyer son index.
        print("je cherche le roi blanc puis j'analyse le plateau")
    
    if connaitreTour(echiquier_a_analyser) == "Noir":
        # chercher le roi noir sur l'échiquier et renvoyer son index
        print("je cherche le roi noir puis j'analyse le plateau")