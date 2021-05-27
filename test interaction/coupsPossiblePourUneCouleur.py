from Classe_Moteur import *

class Bot:
    
    def __init__(self):
        paquet_donner=self.lesDonnerEuristique()
        
        valeur_pion=paquet_donner[0]
        valeur_tour=paquet_donner[1]
        valeur_cavalier=paquet_donner[2]
        valeur_fou=paquet_donner[3]
        valeur_reine=paquet_donner[4]
        valeur_roi=paquet_donner[5]
        
        cottient_agrésiviter=paquet_donner[6]
        cottient_défencife=paquet_donner[7]
        cottient_protection=paquet_donner[8]
        cottient_roi=paquet_donner[9]
        
        valeur_case_roi=paquet_donner[10]

    def tousCoupsPossible(self, case, echiquier):
        liste_coups = []
        if echiquier[0][case[0]][case[1]] != []:
            if echiquier[0][case[0]][case[1]][0][0] == "F" or "Q":
                # on cherche tous les cases possible sur lequel le fou peut aller
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (1,1)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (1,-1)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (-1,-1)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (-1,1)))
            if echiquier[0][case[0]][case[1]][0][0] == "T" or "Q":
                # on cherche toutes les cases possible sur lequel la tour peut aller
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (0,1)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (1,0)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (-1,0)))
                liste_coup.append(toutesCasesAvantLaProchainePiece(case, (0,-1)))
            if echiquier[0][case[0]][case[1]][0][0] == "P":
                if echiquier[1] == 0: # si il s'agit du premier tour
                    liste.coup.append()
                # on cherche toutes les cases possible sur lequel le pion peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "K":
                # on cherche toutes les cases possible sur lequel le pion peut aller
            if echiquier[0][case[0]][case[1]][0][0] == "C":
                # on cherche toutes les cases possible sur lequel le cavalier peut aller


    def coupsPossiblePourUneCouleur(self, couleur, echiquier):
        liste_coups = []
        coupsPossibleCouleur = []
        for x in range(8) :
            for y in range(8): 
               
        
                    
                pion_candidat = echiquier[0][x][y]
                    
                if pion_candidat != []:
                    if pion_candidat[0][1] == couleur:
                        coupsPossibleCouleur += tousCoupsPossible((x,y), echiquier)
        return coupsPossibleCouleur
    
    
    def lEtoileDuDanger(self,une_case,piece,echiquier):
            
            # on créé les variable qui vont étre return
            
            les_case_du_roi_adverse_prise=[]
            les_case_qui_tattaque=[]
            les_case_que_tu_attaque=[]
            les_case_que_tu_protege=[]
            
            #on definie tout les type de mouvement possible
            position_du_roi_adverse=interface.moteur.positionPiece("K"+interface.moteur.lAutreJoueur(piece[1]),echiquier)
            
            mouvement_cavalier=interface.moteur.mouvementCavalier()
            
            mouvement_offensife_pion=interface.moteur.mouvementAufensifPion(piece[1])
            
            mouvement_roi=interface.moteur.mouvementRoi()
            
            directions_type_tour=interface.moteur.directionTour()
            
            directions_type_fou=interface.moteur.directionFou()
            
            
            #on créé la liste des case de control du roi adverce
            les_case_de_control_roi_adverce=[]
            direction_de_control_roi_adverce=[]
            for un_mouvement_de_roi in mouvement_roi:
                if -1 < position_roi[0]+un_mouvement_de_roi[0]<8 and -1 < position_roi[1]+un_mouvement_de_roi[1]<8  :
                    les_case_de_control_roi_adverce.apend((position_roi[0]+un_mouvement_de_roi[0],position_roi[1]+un_mouvement_de_roi[1]))
                    direction_de_control_roi_adverce.append(un_mouvement_de_roi)
            
            
            #on teste si le roi protége la case               
            for un_mouvement_de_roi in mouvement_roi :
                if -1 < une_case[0]+un_mouvement_de_roi[0]<8 and -1 < une_case[1]+un_mouvement_de_roi[1]<8  :
                    if not echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]==[]:
                        if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]== ["K"+piece[1]]:
                            les_case_qui_tattaque.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                        if piece[0]=="k":
                            if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]==piece[1]:
                                les_case_que_tu_protege.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                            else:
                                les_case_que_tu_attaque.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                    if piece[0]=="k":
                        for une_case_de_roi in les_case_de_control_roi_adverce:
                            if (une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]) == une_case_de_roi:
                                les_case_du_roi_adverse_prise.append(une_case_de_roi)
            
            
            
            #on teste si le cavalier protége la case
            for un_mouvement_de_cavalier in mouvement_cavalier:
                if -1 < une_case[0]+un_mouvement_de_cavalier[0]<8 and -1 < une_case[1]+un_mouvement_de_cavalier[1]<8  :               
                    if not echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==[]:
                        if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==["C"+piece[1]]:
                            les_case_qui_tattaque.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                        if piece[0] == "C":
                            if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]][0][1] == piece[1] :
                                les_case_que_tu_protege.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                            else:
                                les_case_que_tu_attaque.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                    if piece[0]=="k":
                        for une_case_de_roi in les_case_de_control_roi_adverce:
                            if (une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]) == une_case_de_roi:
                                les_case_du_roi_adverse_prise.append(une_case_de_roi)
                                
                                
            #on teste si un pion protége la case
            for un_mouvement_de_pion in mouvement_offensife_pion:
                if 8 > une_case[0]+un_mouvement_de_pion[0]> -1 and 8>une_case[1]-un_mouvement_de_pion[1]> -1 :
                    if not echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]+un_mouvement_de_pion[1]]==[]:
                        if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]+un_mouvement_de_pion[1]]==["P"+piece[1]]:
                            les_case_qui_tattaque.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]+un_mouvement_de_pion[1]))
                        if piece[0]=="P":
                            if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]-un_mouvement_de_pion[1]][0][1]==piece[1]:
                                les_case_que_tu_protege.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]+un_mouvement_de_pion[1]))
                            else:
                                les_case_que_tu_attaque.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]+un_mouvement_de_pion[1]))
                    if piece[0]=="k":
                        for une_case_de_roi in les_case_de_control_roi_adverce:
                            if (une_case[0]+un_mouvement_de_pion[0],une_case[1]+un_mouvement_de_pion[1]) == une_case_de_roi:
                                les_case_du_roi_adverse_prise.append(une_case_de_roi)
           
                                       
                    
            #on teste si la tour ou les mouvement aurisontal/vertical de la rene  protége la case   
            for une_direction_type_tour in directions_type_tour:
                la_prochaine_piece=interface.moteur.getNextePiece(une_direction_type_tour)
                if not echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]]==[]:
                    if echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]]==["T"+piece[1]] or ["Q"+piece[1]]:
                        les_case_qui_tattaque.append(la_prochaine_piece)
                    if piece[0]=="T" or "Q":
                        if echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]][0][1]==piece[1]:
                            les_case_que_tu_protege.append(la_prochaine_piece)
                        else:
                            les_case_que_tu_attaque.append(la_prochaine_piece)
            if piece[0]=="T" or "Q":
                for une_case_roi_adverse in les_case_de_control_roi_adverce:
                    for une_direction_type_tour in directions_type_tour:
                        if interface.moteur.direction(une_case_roi_adverse,une_case)==une_direction_type_tour:
                            les_case_de_la_direction=interface.moteur.direction.toutesCasesAvantLaProchainePiece(une_case,interface.moteur.direction(une_case_roi_adverse,une_case))
                            for une_case_de_la_direction in les_case_de_la_direction :
                                if une_case_de_la_direction == une_case_roi_adverse:
                                    les_case_du_roi_adverse_prise.append(une_case_roi_adverse)
                            if echiquier[0][les_case_de_la_direction[-1][0]][les_case_de_la_direction[-1][1]]==["k"+piece[1]]:
                                les_case_du_roi_adverse_prise.append(une_case_roi_adverse)
                            
                                
                            
                                    
                        
                        
            #on teste si le fou ou les coup diagonal de la rene protége la case
            for une_direction_type_fou in directions_type_fou:
                la_prochaine_piece=interface.moteur.getNextePiece(une_direction_type_fou)
                if not echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]]==[]:
                    if echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]]==["F"+piece[1]] or ["Q"+piece[1]]:
                        les_case_qui_tattaque.append(la_prochaine_piece)
                    if piece[0]=="F" or "Q":
                        if echiquier[0][la_prochaine_piece[0]][la_prochaine_piece[1]][0][1]==piece[1]:
                            les_case_que_tu_protege.append(la_prochaine_piece)
                        else:
                            les_case_que_tu_attaque.append(la_prochaine_piece)
            
            if piece[0]=="F" or "Q":
                for une_case_roi_adverse in les_case_de_control_roi_adverce:
                    for une_direction_type_fou in directions_type_fou:
                        if interface.moteur.direction(une_case_roi_adverse,une_case)==une_direction_type_fou:
                            les_case_de_la_direction=interface.moteur.direction.toutesCasesAvantLaProchainePiece(une_case,interface.moteur.direction(une_case_roi_adverse,une_case))
                            for une_case_de_la_direction in les_case_de_la_direction :
                                if une_case_de_la_direction == une_case_roi_adverse:
                                    les_case_du_roi_adverse_prise.append(une_case_roi_adverse)
                            if echiquier[0][les_case_de_la_direction[-1][0]][les_case_de_la_direction[-1][1]]==["k"+piece[1]]:
                                les_case_du_roi_adverse_prise.append(une_case_roi_adverse)
                  
                  
                  
            return (les_case_qui_tattaque,les_case_que_tu_attaque,les_case_que_tu_protege,les_case_du_roi_adverse_prise)

    def applicationEuristiqueSurUnCoup(self,un_coup,les_donner_du_coup,un_echiquier):
            
        valeur_case_depart=self.valeur_piece_case(un_coup[0],un_echiquier)
        valeur_coup=0
        
        valeur_coup+=(len(les_donner_du_coup[0])*cottient_défencife*valeur_case_depart)
        

        for une_case_que_tu_attaque in les_donner_du_coup[1]:
            valeur_coup+=self.valeur_piece_case(une_case_que_tu_attaque,un_echiquier)*cottient_agrésiviter
        
        for une_case_que_tu_proege in les_donner_du_coup[2]:
            valeur_coup+=self.valeur_piece_case(une_case_que_tu_proege,un_echiquier)*cottient_protection
            
        for une_case_que_tu_bloque in les_donner_du_coup[3]:
            valeur_coup+=self.valeur_piece_case(une_case_que_tu_bloque,un_echiquier)
                
        if un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="K":
            valeur_coup*=cottient_roi
            
        if un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="P":
            valeur_coup+=(valeur_pion*cottient_défencife-valeur_reine*cottient_défencife)
        
            
        return valeur_coup
            
    def valeur_piece_case(self,une_case,un_echiquier):
        
        if un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="K":
            valeur_de_la_piece=self.valeur_roi
            
        elif un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="Q":
            valeur_de_la_piece=self.valeur_reine
            
        elif un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="T":
            valeur_de_la_piece=self.valeur.tour
            
        elif un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="F":
            valeur_de_la_piece=self.valeur.fou
            
        elif un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="P":
            valeur_de_la_piece=self.valeur.pion
            
        elif un_echiquiée[0][une_case[0]][une_case[1]][0][0]=="C":
            valeur_de_la_piece=self.valeur.cavalier
