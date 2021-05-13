class Moteur:
    def __init__(self,les_joueurs):
        """mette en place la partie
        _________________________
        demande les_joueur un tuple  ("R"ou"J")("R"ou"J")"""
        self.echiquier=[[[["TB"],["PB"],[],[],[],[],["PN"],["TN"]],[["CB"],["PB"],[],[],[],[],["PN"],["CN"]],[["FB"],["PB"],[],[],[],[],["PN"],["FN"]],[["KB"],["PB"],[],[],[],[],["PN"],["KN"]],[["QB"],["PB"],[],[],[],[],["PN"],["QN"]],[["FB"],["PB"],[],[],[],[],["PN"],["FN"]],[["CB"],["PB"],[],[],[],[],["PN"],["CN"]],[["TB"],["PB"],[],[],[],[],["PN"],["TN"]]],0]
        self.Blanc=les_joueurs[0]
        self.Noire=les_joueurs[1]
        self.etat_partie="en cours"
        
        
        
        
    def echequeEtMat(self,joueur):
        """methode de moteur qui permet de savoir si un joueur est en echeque et mat
        ______________________
        demande
        un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        et unn mouvement sous la forme d un tuple contenant 2 tuple qui constienne 2 int entre 0 et 7 comprie
        ex ((3,6),(4,1))
        _______________________
        return
        True   ou False
        """
        le_joueur_est_mat=True
        composante_de_l_echeque=self.echequrAuRoi(joueur,self.getEchiquier())
        echiquier=self.getEchiquier()
        
        #esque e joueur est en echeque
        
        if composante_de_l_echeque[0]==False:
           le_joueur_est_mat=False
            
        #esque une piece peut manger 
        if le_joueur_est_mat==True :
            if len(composante_de_l_echeque[1])==1:
                if self.caseProtegePar(composante_de_l_echeque[1][0],joueur):
                    le_joueur_est_mat=False
                    
        #esque une piece peut ce mettre entre le roi et l'agréseur
        if le_joueur_est_mat==True :
            if len(composante_de_l_echeque[1])==1:
                if echiquier[0][composante_de_l_echeque[1][0][0]][composante_de_l_echeque[1][0][1]][0][0] =="Q" or "T" or "F":
                    case_intermediaire=self.toutesCaseAvantLaProchainePiece(composante_de_l_echeque[1][0],self.direction(self.positionPiece("K"+joueur,echiquier),composante_de_l_echeque[1][0]),echiquier)
                    if len(case_intermediaire)> 0:
                        for x in case_intermediaire:
                            if self.caseAxeiblePar(x,joueur,echiquier):
                                le_joueur_est_mat=False
                        
                     
        #esque le roix peut fuire
        
            
        if le_joueur_est_mat==True:
            position_roi=self.positionPiece("K"+joueur,echiquier)
            mouvement_vers_les_case_adjasente_a_une_case=[(-1,-1),(-1,0),(-1,1),(0,1),(-0,-1),(1,-1),(1,1),(1,0)]
            les_case_qui_mette_en_echeque=composante_de_l_echeque[1]
            case_echapatoire=[]
            
            for x in les_case_qui_mette_en_echeque:
                if echiquier[0][x[0]][x[1]][0][0] =="Q" or "T" or "F":
                    for v in range(len(mouvement_vers_les_case_adjasente_a_une_case)) :
                        direction_attaque=self.direction(position_roi,x) 
                        if mouvement_vers_les_case_adjasente_a_une_case[v]==self.direction(self.positionPiece("K"+joueur,echiquier),x):
                            del mouvement_vers_les_case_adjasente_a_une_case[v]
                        elif mouvement_vers_les_case_adjasente_a_une_case[v]==self.directionOposer(self.direction(self.positionPiece("K"+joueur,echiquier),x)):
                            del mouvement_vers_les_case_adjasente_a_une_case[v]
                            P=3
            
            for mouvement in mouvement_vers_les_case_adjasente_a_une_case :
                if position_roi[0]+mouvement[0]<8 and position_roi[0]+mouvement[0]> -1 and position_roi[1]+mouvement[1]<8 and position_roi[1]+mouvement[1] > -1 :
                        case_echapatoire.append((position_roi[0]+mouvement[0],position_roi[1]+mouvement[1]))
            x=0
            while le_joueur_est_mat==True and len(case_echapatoire[x])>x:
                if echiquier[0][case_echapatoire[x][0]][case_echapatoire[x][1]] ==[]:
                    if not self.ProtegePar(case_echapatoire[x],self.lAutreJoueur(joueur),echiquier):
                         le_joueur_est_mat==False
                    
                elif echiquier[0][case_echapatoire[x][0]][case_echapatoire[x][1]][0][1]!=joueur:
                    if not self.ProtegePar(case_echapatoire[x],self.lAutreJoueur(joueur),echiquier):
                         le_joueur_est_mat==False
                
                x+=1
                              
            
            
        return  le_joueur_est_mat
    
    
    
    def direction(self,case1,cacse2):
        
        x=case1[0]-case2[0]
        y=case1[1]-case2[1]
        
        x=x/abs(x)
        y=y/abs(y)
        
        return (x,y)
    
    
    def directionOposer(self,direction):
        """metode de moteur qui donne une direction oposer
        ______________________
        demande
        une direction sous la forme d un tuple contenant 2 int
        ______________________
        return
        une direction sous la forme d un tuple contenant 2 int
        """
        return(direction[0]*-1,direction[1]*-1)
    
    
    
    
    
    
    
    def positionPiece(self,piece,echiquier):
        """méthode de moteur qui permette de determminer pa position d une piece dans un echiquier
        _________________________________
        demande :
        une piece
        ___________________________________
        return
        un tuple de 2 int entre 0 et 7 compris 
        """
         #on determin la position de la piece rechercher
        for x in range(8):
            for y in range (8):
                if echiquier[0][x][y]==[piece]:
                    position_piece =( x,y)
                    
        return position_piece          
                    
                    
                    
    
    def echequrAuRoi(self,joueur,echiquier):
        """méthode de moteur qui permet de déterminer si un roi est en echeque et si oui quelle piece mette le rois en echeque    le tout dans un echiquier donné
        ______________________________
        demande:
    
        un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        
        et un echiquier
        ______________________________
        return:
        renvoie un tuple contenant:
        une valeur boolen True si le roi du joueur est en echeque False si il ne lest pas
        et une liste de tout les case qui mette en echec le roi. cette liste est vide si le roi nest pas en echeque
        
        ex:   (True, [(2, 1), (0, 1)])
        """
    
        #on determin la position du rois rechercher
        position_roi=self.positionPiece("K"+joueur,echiquier)
        
        #on regarde si le rois est en echeque
        le_roi_est_en_echeque = moteur.caseProtegePar(position_roi,moteur.lAutreJoueur(joueur),echiquier)
        
        return le_roi_est_en_echeque
    
      
    
    
    
    
    def lAutreJoueur(self,joueur):
        """methode de moteur qui renvoie le de le joueur adverse de seluis appeller
        _____________________________________
        demande:
        un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        ______________________________________________________________
        return
        un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        """
        if joueur=="B":
            l_autre_joueur="N"
        else:
            l_autre_joueur="B"
        return l_autre_joueur
        
        
        
    
    
    def caseProtegePar(self,une_case,joueur,echiquier):
        """caseControlerPar est une métode de Moteur qui permet de sasvoir si une case est protéger par un joueur definie dans un echiuier définie
        _________________________________________________
        demande une case sou la forme dun tuple de 2 chifre entre 0et7 comprit qui coresponde au cordonner de la dite case
        ex:   (3,7)
        
        et un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        
        et un echiquier
        _____________________
        renvoie un tuple contenant:
        une valeur boolen True si le joueur protége la case False si il ne la protége pas
        et une liste de tout les case qui protége la case. cette liste est vide si la case nest pas protéger par le joueur
        
        ex:   (True, [(2, 1), (0, 1)])

        """
        
        # on créé les variable qui vont étre return
        
        la_case_est_controler_par_le_joueur=False
        
        case_qui_exerce_le_control=[]
        
        #on definie tout les type de mouvement possible
        
        mouvement_cavalier=self.mouvementCavalier()
        
        mouvement_offensife_pion=self.mouvementAufensifPion(joueur)
        
        mouvement_roi=self.mouvementRoi()
        
        directions_type_tour=self.directionTour()
        
        directions_type_fou=self.directionFou()
        
        
        #on definie la position du roi
        
        possistion_roi=self.positionPiece("K"+joueur,echiquier)
        
        #on teste si le cavalier protége la case
        for un_mouvement_de_cavalier in mouvement_cavalier:
            if une_case[0]+un_mouvement_de_cavalier[0]<8 and une_case[0]+un_mouvement_de_cavalier[0]> -1 and une_case[1]+un_mouvement_de_cavalier[1]<8 and une_case[1]+un_mouvement_de_cavalier[1] > -1 :               
                if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==[ "C"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                    
        #on teste si un pion protége la case
        for un_mouvement_de_pion in mouvement_offensife_pion:
            if une_case[0]+un_mouvement_de_pion[0]> -1 and une_case[0]+un_mouvement_de_pion[0]<8 and une_case[1]-un_mouvement_de_pion[1]> -1 and une_case[1]-un_mouvement_de_pion[1]<8:
                if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]-un_mouvement_de_pion[1]]==["P"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]-un_mouvement_de_pion[1]))
                    
        #on teste si le roi protége la case               
        for un_mouvement_de_roi in mouvement_roi :
            if une_case[0]+un_mouvement_de_roi[0]<8 and une_case[0]+un_mouvement_de_roi[0]> -1 and une_case[1]+un_mouvement_de_roi[1]<8 and une_case[1]+un_mouvement_de_roi[1] > -1 :
                if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]== ["K"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                        
                
                
                
        #on teste si la tour ou les mouvement aurisontal/vertical de la rene  protége la case   
        for une_direction_type_tour in directions_type_tour:
            if echiquier[0][self.getNextePiece(une_direction_type_tour)[0]][self.getNextePiece(une_direction_type_tour)[1]]==["T"+joueur] or echiquier[0][self.getNextePiece(une_direction_type_tour)[0]][self.getNextePiece(une_direction_type_tour)[1]]==["Q"+joueur]:
                la_case_est_controler_par_le_joueur=True
                case_qui_exerce_le_control.append(self.getNextePiece(une_direction_type_tour))
                
                    
                    
        #on teste si le fou ou les coup diagonal de la rene protége la case
        for une_direction_type_fou in directions_type_fou:
            if echiquier[0][self.getNextePiece(une_direction_type_fou)[0]][self.getNextePiece(une_direction_type_fou)[1]]==["F"+joueur] or echiquier[0][self.getNextePiece(une_direction_type_fou)[0]][self.getNextePiece(une_direction_type_fou)[1]]==["Q"+joueur]:
                la_case_est_controler_par_le_joueur=True
                case_qui_exerce_le_control.append(self.getNextePiece(une_direction_type_fou))
                
              
        return (la_case_est_controler_par_le_joueur,case_qui_exerce_le_control)
    
    def caseAxeiblePar(self,une_case,joueur,echiquier):
        """caseAxeiblePar est une métode de Moteur qui permet de sasvoir si une case est axésible en 1 coup par un joueur definie dans un echiuier définie
        _________________________________________________
        demande une case sou la forme dun tuple de 2 chifre entre 0et7 comprit qui coresponde au cordonner de la dite case
        ex:   (3,7)
        
        et un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        
        et un echiquier
        _____________________
        renvoie un tuple contenant:
        une valeur boolen True si le joueur peu axéder a la case False si il ne peu pas
        et une liste de tout les case qui peuve axéder a la case en 1coup  la case. cette liste est vide si la case nest pas protéger par le joueur
        
        ex:   (True, [(2, 1), (0, 1)])

        """
        
        # on créé les variable qui vont étre return
        
        la_case_est_controler_par_le_joueur=False
        
        case_qui_exerce_le_control=[]
        
        #on definie tout les type de mouvement possible
        
        mouvement_cavalier=self.mouvementCavalier()
        
        mouvement_passife_pion=self.mouvementPassifePion(joueur)
        
        mouvement_roi=self.mouvementRoi()
        
        directions_type_tour=self.directionTour()
        
        directions_type_fou=self.directionFou()
        
        
        #on definie la position du roi
        
        possistion_roi=self.positionPiece("K"+joueur,echiquier)
        
        #on teste si le cavalier protége la case
        for un_mouvement_de_cavalier in mouvement_cavalier:
            if une_case[0]+un_mouvement_de_cavalier[0]<8 and une_case[0]+un_mouvement_de_cavalier[0]> -1 and une_case[1]+un_mouvement_de_cavalier[1]<8 and une_case[1]+un_mouvement_de_cavalier[1] > -1 :               
                if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==[ "C"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                    
        #on teste si un pion protége la case
        for un_mouvement_de_pion in mouvement_passife_pion:
            if une_case[0]+un_mouvement_de_pion[0]> -1 and une_case[0]+un_mouvement_de_pion[0]<8 and une_case[1]-un_mouvement_de_pion[1]> -1 and une_case[1]-un_mouvement_de_pion[1]<8:
                if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]-un_mouvement_de_pion[1]]==["P"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]-un_mouvement_de_pion[1]))
                    
        #on teste si le roi protége la case               
        for un_mouvement_de_roi in mouvement_roi :
            if une_case[0]+un_mouvement_de_roi[0]<8 and une_case[0]+un_mouvement_de_roi[0]> -1 and une_case[1]+un_mouvement_de_roi[1]<8 and une_case[1]+un_mouvement_de_roi[1] > -1 :
                if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]== ["K"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                        
                
                
                
        #on teste si la tour ou les mouvement aurisontal/vertical de la rene  protége la case   
        for une_direction_type_tour in directions_type_tour:
            if echiquier[0][self.getNextePiece(une_direction_type_tour)[0]][self.getNextePiece(une_direction_type_tour)[1]]==["T"+joueur] or echiquier[0][self.getNextePiece(une_direction_type_tour)[0]][self.getNextePiece(une_direction_type_tour)[1]]==["Q"+joueur]:
                la_case_est_controler_par_le_joueur=True
                case_qui_exerce_le_control.append(self.getNextePiece(une_direction_type_tour))
                
                    
                    
        #on teste si le fou ou les coup diagonal de la rene protége la case
        for une_direction_type_fou in directions_type_fou:
            if echiquier[0][self.getNextePiece(une_direction_type_fou)[0]][self.getNextePiece(une_direction_type_fou)[1]]==["F"+joueur] or echiquier[0][self.getNextePiece(une_direction_type_fou)[0]][self.getNextePiece(une_direction_type_fou)[1]]==["Q"+joueur]:
                la_case_est_controler_par_le_joueur=True
                case_qui_exerce_le_control.append(self.getNextePiece(une_direction_type_fou))
                
              
        return (la_case_est_controler_par_le_joueur,case_qui_exerce_le_control)
    

    def mouvementPassifePion(self,joueur):
        """fonctin de moteur qu permet de conaitre les mouvement d ataque des pion selon leur couleur
        ____________
        demande la couleur des pion sous la forme d une str "B"   pour les pion blanc  "N" pour les pion noires
        ______________
        renvoie une liste de vecteur de deplasement
        """
        
        if joueur=="B":
            mouvement_pion=[(0,1)]
        else:
            mouvement_pion=[(0,-1)]
            
        return mouvement_pion
          
          
          
    def mouvementCavalier(self):
        return [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] 
    
    
    
    
    
    def mouvementAufensifPion(self,joueur):
        """fonctin de moteur qu permet de conaitre les mouvement d ataque des pion selon leur couleur
        ____________
        demande la couleur des pion sous la forme d une str "B"   pour les pion blanc  "N" pour les pion noires
        ______________
        renvoie une liste de vecteur de deplasement
        """
        
        if joueur=="B":
            mouvement_pion=[(1,1),(-1,1)]
        else:
            mouvement_pion=[(1,-1),(-1,-1)]
            
        return mouvement_pion
          
    def mouvementCavalier(self):
        return [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    
    
    
    def mouvementRoi(self):
        return [(-1,-1),(-1,0),(-1,1),(0,1),(-0,-1),(1,-1),(1,1),(1,0)]
    
    
    def directionTour(self):
        return [(1,0),(0,1),(0,-1),(-1,0)]
    
    
    def directionFou(self):
        return [(1,1),(-1,1),(1,-1),(-1,-1)]
              
          
          
    def getEchiquier(self):
        """renvoie echiquier"""
        return self.echiquier
    
    
    
    
    def getLesJoueur(self):
        """renvoie les_joueur"""
        return((self.Blanc),(self.Noire))



    def getEtatPartie(self):
        """renvoie etat_partie"""
        return self.etat_partie
#bouchonage   
    
    
    
    def getNextePiece(self,pomme):
        return (5,5)
    
 
    def coupValide(self,un_coup):
        return(False)
    


    def gestionCoupValider(self,e):
        return  
    

    
moteur=Moteur(("J","R"))
print(moteur.caseProtegePar((1,2),"B",moteur.echiquier))
moteur.echequeEtMat('B')
