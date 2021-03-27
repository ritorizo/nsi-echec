from connaitre_tour import connaitre_tour

echiquier =[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], 1] # il s'agit d'un exemple d'échiquier.

def mise_en_echec(echiquier_a_analyser):
    
    if connaitre_tour(echiquier_a_analyser) == "Blanc":
        # chercher le roi blanc sur l'échiquier et renvoyer son index.
        print("je cherche le roi blanc puis j'analyse le plateau")
    
    if connaitre_tour(echiquier_a_analyser) == "Noir":
        # chercher le roi noir sur l'échiquier et renvoyer son index
        print("je cherche le roi noir puis j'analyse le plateau")