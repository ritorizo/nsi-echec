echiquier =[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["QB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["KB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], 1] # il s'agit d'un exemple d'échiquier.

def connaitre_tour(echiquier_a_analyser):
    '''
    Permet de savoir à qui est le tour sur l'échiquier.
    ----------
    renvoie "Blanc" si c'est un tour paire.
    renvoie "Noir" si c'est un tour impaire.
    ----------
    Peut être utilisé lors d'un besoin de savoir qui a joué
    '''

    if echiquier[-1] % 2 == 0:
        return "Blanc"
    
    if echiquier[-1] % 2 != 0:
        return "Noir"