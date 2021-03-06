from pygame import encode_file_path


class Moteur:

    echiquier = [[[["TB"],[],["KN"],[],[],[],[],[]], [[],[],[],[],["KB"],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]], [[],[],[],[],[],["QB"],[],[]], [[],[],[],[],[],[],[],[]], [['PB'],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[]]], 0]

    def __init__(self,les_joueurs):
        """mette en place la partie
        _________________________
        demande les_joueur un tuple  ("R"ou"J")("R"ou"J")"""
        self.echiquier=[[[["TB"],["PB"],[],[],[],[],["PN"],["TN"]],[["CB"],["PB"],[],[],[],[],["PN"],["CN"]],[["FB"],["PB"],[],[],[],[],["PN"],["FN"]],[["QB"],["PB"],[],[],[],[],["PN"],["KN"]],[["KB"],["PB"],[],[],[],[],["PN"],["QN"]],[["FB"],["PB"],[],[],[],[],["PN"],["FN"]],[["CB"],["PB"],[],[],[],[],["PN"],["CN"]],[["TB"],["PB"],[],[],[],[],["PN"],["TN"]]],0]
        self.Blanc=les_joueurs[0]
        self.Noire=les_joueurs[1]
        self.etat_partie="en cours"
        
        
        
        
    def echecEtMat(self,joueur):
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
        composante_de_l_echeque=self.echequeAuRoi(joueur,self.getEchiquier())
        echiquier=self.getEchiquier()
        
        #esque e joueur est en echeque
        
        if composante_de_l_echeque[0]==False:
           le_joueur_est_mat=False
            
        #esque une piece peut manger 
        if le_joueur_est_mat==True :
            if len(composante_de_l_echeque[1])==1:
                if self.caseProtegePar(composante_de_l_echeque[1][0],joueur):
                    le_joueur_est_mat=False
                    
        #esque une piece peut ce mettre entre le roi et l'agr??seur
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
        
        while c2 ==False :
            if x%2==0 and y%2==0:
                x=x/2
                y=y/2
            else:
                c2==True

        while c5 ==False :
            if x%5==0 and y%5==0:
                x=x/5
                y=y/5
            else:
                c5==True

        while c3 ==False :
            if x%3==0 and y%3==0:
                x=x/3
                y=y/3
            else:
                c3==True

        while c7 ==False :
            if x%7==0 and y%7==0:
                x=x/7
                y=y/7
            else:
                c7==True
        
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
    
    
    
    
    
    
    
    #TODO d??vider de se que position_piece renvois si elle trouve rien
    def positionPiece(self,piece,echiquier):
        """m??thode de moteur qui permette de determminer pa position d une piece dans un echiquier
        _________________________________
        demande :
        une piece
        ___________________________________
        return
        un tuple de 2 int entre 0 et 7 compris' 
        """
        #on determin la position de la piece rechercher
        position_piece = (-1, -1)
        for x in range(8):
            for y in range (8):
                if echiquier[0][x][y]==[piece]:
                    position_piece =(x,y)
                    
        return position_piece          
                    
                    
                    
    
    def echequeAuRoi(self,joueur,echiquier):
        """m??thode de moteur qui permet de d??terminer si un roi est en echeque et si oui quelle piece mette le rois en echeque    le tout dans un echiquier donn??
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
        le_roi="K"+joueur
        position_roi=self.positionPiece(le_roi,echiquier)
        
        #on regarde si le rois est en echeque
        le_roi_est_en_echeque = self.caseProtegePar(position_roi,self.lAutreJoueur(joueur),echiquier)
        
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
        """caseControlerPar est une m??tode de Moteur qui permet de sasvoir si une case est prot??ger par un joueur definie dans un echiuier d??finie
        _________________________________________________
        demande une case sou la forme dun tuple de 2 chifre entre 0et7 comprit qui coresponde au cordonner de la dite case
        ex:   (3,7)
        
        et un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        
        et un echiquier
        _____________________
        renvoie un tuple contenant:
        une valeur boolen True si le joueur prot??ge la case False si il ne la prot??ge pas
        et une liste de tout les case qui prot??ge la case. cette liste est vide si la case nest pas prot??ger par le joueur
        
        ex:   (True, [(2, 1), (0, 1)])

        """
        
        # on cr???? les variable qui vont ??tre return
        
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
        
        #on teste si le cavalier prot??ge la case
        for un_mouvement_de_cavalier in mouvement_cavalier:
            if une_case[0]+un_mouvement_de_cavalier[0]<8 and une_case[0]+un_mouvement_de_cavalier[0]> -1 and une_case[1]+un_mouvement_de_cavalier[1]<8 and une_case[1]+un_mouvement_de_cavalier[1] > -1 :               
                if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==[ "C"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                    
        #on teste si un pion prot??ge la case
        for un_mouvement_de_pion in mouvement_offensife_pion:
            if une_case[0]+un_mouvement_de_pion[0]> -1 and une_case[0]+un_mouvement_de_pion[0]<8 and une_case[1]-un_mouvement_de_pion[1]> -1 and une_case[1]-un_mouvement_de_pion[1]<8:
                if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]-un_mouvement_de_pion[1]]==["P"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]-un_mouvement_de_pion[1]))
                    
        #on teste si le roi prot??ge la case               
        for un_mouvement_de_roi in mouvement_roi :
            if une_case[0]+un_mouvement_de_roi[0]<8 and une_case[0]+un_mouvement_de_roi[0]> -1 and une_case[1]+un_mouvement_de_roi[1]<8 and une_case[1]+un_mouvement_de_roi[1] > -1 :
                if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]== ["K"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                        
                
                
                
        #on teste si la tour ou les mouvement aurisontal/vertical de la rene  prot??ge la case   
        for une_direction_type_tour in directions_type_tour:
            if not echiquier[0][self.getNextPiece(une_case,une_direction_type_tour)[0]][self.getNextPiece(une_case,une_direction_type_tour)] == [] :
                if echiquier[0][self.getNextPiece(une_case,une_direction_type_tour)[0]][self.getNextPiece(une_case,une_direction_type_tour)]==["T"+joueur] or echiquier[0][self.getNextPiece(une_case,une_direction_type_tour)[0]][self.getNextPiece(une_case,une_direction_type_tour)[1]]==["Q"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append(self.getNextPiece(une_case,une_direction_type_tour))
                
                    
                    
        #on teste si le fou ou les coup diagonal de la rene prot??ge la case
        for une_direction_type_fou in directions_type_fou:
            if not echiquier[0][self.getNextPiece(une_case,une_direction_type_fou)[0]][self.getNextPiece(une_case,une_direction_type_fou)] == []:
                if echiquier[0][self.getNextPiece(une_case,une_direction_type_fou)[0]][self.getNextPiece(une_case,une_direction_type_fou)]==["F"+joueur] or echiquier[0][self.getNextPiece(une_case,une_direction_type_fou)[0]][self.getNextPiece(une_case,une_direction_type_fou)[1]]==["Q"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append(self.getNextPiece(une_case,une_direction_type_fou))
                
              
        return (la_case_est_controler_par_le_joueur,case_qui_exerce_le_control)
    
    def caseAxeiblePar(self,une_case,joueur,echiquier):
        """caseAxeiblePar est une m??tode de Moteur qui permet de sasvoir si une case est ax??sible en 1 coup par un joueur definie dans un echiuier d??finie
        _________________________________________________
        demande une case sou la forme dun tuple de 2 chifre entre 0et7 comprit qui coresponde au cordonner de la dite case
        ex:   (3,7)
        
        et un joueur sous la forme de une str soit "B" pour le joueur blanc  soit "N" pour le joueur noire
        
        et un echiquier
        _____________________
        renvoie un tuple contenant:
        une valeur boolen True si le joueur peu ax??der a la case False si il ne peu pas
        et une liste de tout les case qui peuve ax??der a la case en 1coup  la case. cette liste est vide si la case nest pas prot??ger par le joueur
        
        ex:   (True, [(2, 1), (0, 1)])

        """
        
        # on cr???? les variable qui vont ??tre return
        
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
        
        #on teste si le cavalier prot??ge la case
        for un_mouvement_de_cavalier in mouvement_cavalier:
            if une_case[0]+un_mouvement_de_cavalier[0]<8 and une_case[0]+un_mouvement_de_cavalier[0]> -1 and une_case[1]+un_mouvement_de_cavalier[1]<8 and une_case[1]+un_mouvement_de_cavalier[1] > -1 :               
                if echiquier[0][une_case[0]+un_mouvement_de_cavalier[0]][une_case[1]+un_mouvement_de_cavalier[1]]==[ "C"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_cavalier[0],une_case[1]+un_mouvement_de_cavalier[1]))
                    
        #on teste si un pion prot??ge la case
        for un_mouvement_de_pion in mouvement_passife_pion:
            if une_case[0]+un_mouvement_de_pion[0]> -1 and une_case[0]+un_mouvement_de_pion[0]<8 and une_case[1]-un_mouvement_de_pion[1]> -1 and une_case[1]-un_mouvement_de_pion[1]<8:
                if echiquier[0][une_case[0]+un_mouvement_de_pion[0]][une_case[1]-un_mouvement_de_pion[1]]==["P"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_pion[0],une_case[1]-un_mouvement_de_pion[1]))
                    
        #on teste si le roi prot??ge la case               
        for un_mouvement_de_roi in mouvement_roi :
            if une_case[0]+un_mouvement_de_roi[0]<8 and une_case[0]+un_mouvement_de_roi[0]> -1 and une_case[1]+un_mouvement_de_roi[1]<8 and une_case[1]+un_mouvement_de_roi[1] > -1 :
                if echiquier[0][une_case[0]+un_mouvement_de_roi[0]][une_case[1]+un_mouvement_de_roi[1]]== ["K"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append((une_case[0]+un_mouvement_de_roi[0],une_case[1]+un_mouvement_de_roi[1]))
                        
                
                
                
        #on teste si la tour ou les mouvement aurisontal/vertical de la rene  prot??ge la case   
        for une_direction_type_tour in directions_type_tour:
            if not echiquier[0][self.getNextePiece(une_case,une_direction_type_tour)[0]][self.getNextePiece(une_case,une_direction_type_tour)] == []:
                if echiquier[0][self.getNextePiece(une_case,une_direction_type_tour)[0]][self.getNextePiece(une_case,une_direction_type_tour)]==["T"+joueur] or echiquier[0][self.getNextePiece(une_case,une_direction_type_tour)[0]][self.getNextePiece(une_case,une_direction_type_tour)[1]]==["Q"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append(self.getNextePiece(une_case,une_direction_type_tour))
                
                    
                    
        #on teste si le fou ou les coup diagonal de la rene prot??ge la case
        for une_direction_type_fou in directions_type_fou:
            if not echiquier[0][self.getNextePiece(une_case,une_direction_type_fou)[0]][self.getNextePiece(une_case,une_direction_type_fou)] == []:
                if echiquier[0][self.getNextePiece(une_case,une_direction_type_fou)[0]][self.getNextePiece(une_case,une_direction_type_fou)]==["F"+joueur] or echiquier[0][self.getNextePiece(une_case,une_direction_type_fou)[0]][self.getNextePiece(une_case,une_direction_type_fou)[1]]==["Q"+joueur]:
                    la_case_est_controler_par_le_joueur=True
                    case_qui_exerce_le_control.append(self.getNextePiece(une_case,une_direction_type_fou))
                
              
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
    
    
    def connaitreTour(self,echiquier_a_analyser):
        '''
        Permet de savoir ?? qui est le tour sur l'??chiquier.
        ----------
        renvoie "Blanc" si c'est un tour paire.
        renvoie "Noir" si c'est un tour impaire.
        ----------
        Peut ??tre utilis?? lors d'un besoin de savoir qui a jou??
        '''

        if echiquier_a_analyser[-1] % 2 == 0:
            return "Blanc"
        else: 
            return "Noir"

    #def sauvegarde(self,echiquier_a_sauvegarder):
#
    #    sauvegarde_tour = echiquier_a_sauvegarder[-1]
    #    sauvegarde_tour = str(sauvegarde_tour)
    #    echiquier_a_sauvegarder = str(echiquier_a_sauvegarder)
    #    fichier=open('logs/sauvegarde_echec.txt','a+')
    #    fichier.write('Tour ')
    #    fichier.write(sauvegarde_tour)
    #    fichier.write(' : ')
    #    fichier.write(echiquier_a_sauvegarder)
    #    fichier.write( '\n' )
    #    fichier.close
    #    print("Sauvegarde du tour effectu??")

    def gestionCoupValider(self,mouvement): # mouvement entr??e sous la forme ((0,5),(1,6))

        #self.sauvegarde(self.echiquier)
        
        # d??placement du pion avec les coordon??es entr?? par mouvement. (sur les deux prochaines lignes)
        self.echiquier[0][mouvement[1][0]][mouvement[1][1]]=self.echiquier[0][mouvement[0][0]][mouvement[0][1]]
        self.echiquier[0][mouvement[0][0]][mouvement[0][1]]=[]
        
        for x in range(7): # v??rifie si un pion va ?? dame
            if self.echiquier[0][x][0] == ["PN"]:
                self.echiquier[0][x][0] = ["QN"]
            
            if self.echiquier[0][x][7] == ["PB"]:
                self.echiquier[0][x][7] = ["QB"]
        

#        if self.echequeEtMat(self.connaitreTour) == True:
#            if self.connaitreTour(self.echiquier) == "Blanc":
#                self.etat_partie = "Noir a perdu"
#            else: 
#                self.etat_partie = "Blanc a perdu"


        self.echiquier[-1]+= 1 # on ajoute 1 au compteur de tour.

        print(self.echiquier)
        print("gestionCoupValider effectu??")

    def getNextPiece(self,coordon??es_de_pi??ce, direction_a_analyser):
        piece_proche = ()
        x = coordon??es_de_pi??ce[0]
        y = coordon??es_de_pi??ce[1]

        while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pi??ce la plus proche n'est pas trouv?? et que le bord du plateau n'est pas atteint, faire :
            piecel=(x,y)
            x += direction_a_analyser[0]
            y += direction_a_analyser[1]
            
            if not (x > 7 or y > 7 or x < 0 or y < 0):
                if self.echiquier[0][x][y] != []:
                    piece_proche = (x,y)
                    print("pi??ce la plus proche enregistr??")
            else:
                piece_proche=piecel
                print("mur rencontr??")
        return piece_proche

    def toutesCasesAvantLaProchainePiece(self,coordon??es_de_pi??ce, direction_a_analyser):
        piece_proche = ()
        x = coordon??es_de_pi??ce[0]
        y = coordon??es_de_pi??ce[1]
        tableau =[]

        while piece_proche == () and x <= 7 and y <= 7 and x>= 0 and x >= 0: # tant que la pi??ce la plus proche n'est pas trouv?? et que le bord du plateau n'est pas atteint, faire :
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
    def couleurTour(self):
        """Cette m??thdoe renvois la couleur du joueur dont c'est le tour
        ----
        retour : 'N' si le joueur qui joue est noir et 'B' si le joueur qui jou est blanc
        """
        result = 'N'
        if (self.echiquier[1] % 2 == 0) :
            result = 'B'
   
        return result
   
    def formateEchiquier(self):
        """Formate l'??chiquier de mani??re plus propre pour l'utiisation dans coupValide
        ----
        retour : un ??chiquier normal mais les pions ne sont pas dans des sous tables individuel (donc un pion blanc
                 serais "PB" et pas ["PB"].
                 Et les cases sans pi??ce sont repr??sent?? par "  " et non pas par "".
        """
        line = []
        nouveau = [[], self.echiquier[1]]

        for x in range(8):
            line = []
            for y in range(8):
                if ( self.echiquier[0][x][y] == [] ):
                    line.append("  ")
                else:
                    line.append(self.echiquier[0][x][y][0])
            
            nouveau[0].append(line)

        return nouveau

    def coupValide(self, mouvement):
        """Dit si le joueur dont c'est le tour peut d??placer le contenu d'une case a une autre.
        ----
        entr??e : un tuple tel que ((x1, y1), (x2, y2)) avec les x et y des entiers entre 0 et 7 formant les
                 coordon??es de la case 1 et de la case 2.
        ----
        retour : un bool??en True si le joueur peut ??ff??ctuer cette action sinon False.
        """
        x1 = mouvement[0][0]
        y1 = mouvement[0][1]
        x2 = mouvement[1][0]
        y2 = mouvement[1][1]

        echiquier=self.formateEchiquier()
        print(echiquier)
   
        print(x1, y1, x2, y2)
        result = True
   
        # V??rifie que le mouvement ne sort pas de l'??chiquier
        for i in (x1, y1, y2, y2):
            if not(0 <= i <= 7) :
                result = False
   
        # On fait les v??rification g??n??rales.
        if (result == True):

            # V??rifie que le joueur a le droit de s??l??ctioner la pi??ce qu'il a choisi.
            if (echiquier[0][x1][y1][1] != self.couleurTour()):
                result = False
   
            # V??rifie que le joueur n'??saye pas de manger sa propre pi??ce.
            elif (echiquier[0][x2][y2][1] == self.couleurTour()):
                result = False
                
            # V??rifique que la pi??ce ne reste pas sur place.
            elif ( (x1 == x2) and (y1 == y2) ):
                result = False 

        
        # Fait les v??rifications sp??cifiques aux pi??ces 
        piece = echiquier[0][x1][y1][0]
        if (result == True):

            # Verif roi <fait>
            if (piece == 'K'): 
                if ( 2 < ((x1-x2)**2+(y1-y2)**2)):
                    result = False
        
            # Verif reinne <fait>
            elif (piece == 'Q'):
                delta = ((x2-x1), (y2-y1))
                dirrection = (self.signe(delta[0]), self.signe(delta[1]))
                nextpiece = self.getNextPiece((x1, y1), self.dirrection)
                deltaMax = ((nextpice[0]-x1), nextpiece[1]-y1 )

                if (abs(delta[0]) > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                    result == False
            
            # Verif fou <fait>
            elif (piece == 'F'):
                if (estDiagonale(mouvement)):
                    delta = ((x2-x1), (y2-y1))
                    dirrection = (self.signe(delta[0]), self.signe(delta[1]))
                    nextpiece = self.getNextPiece((x1, y1), dirrection)
                    deltaMax = ((nextpice[0]-x1), nextpiece[1]-y1 )

                    if (abs(delta[0]) > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                        result = False
                    else :
                        result = True
                            
            # Verif cavalier <fait>
            elif (piece == 'C'):
                if not(( (x2-x1)**2 + (y2-y1)**2 ) == 5 ): 
                    result = False

            #Verif tour <fait>
            elif (piece == 'T'):
                if (self.estDroit(mouvement)):
                    delta = ((x2-x1), (y2-y1))
                    dirrection = (self.signe(delta[0]), self.signe(delta[1]))
                    nextpiece = self.getNextPiece((x1, y1), dirrection)
                    deltaMax = ((nextpiece[0]-x1), nextpiece[1]-y1 )

                    if (abs(delta[0]) > abs(deltaMax[0])) or (delta[1] > abs(deltaMax[1])):
                        result = False
                   
                            
        
            # Verif pion <fait>
            elif (piece == 'P'):
                # V??rifie le sens du plateau
                facteurSens = 1
                if (self.couleurTour == 'N'):
                    facteurSens = -1
                    
                mouv = ((x2-x1), (y2-y1)*facteurSens)
                
                if ( ( mouv == (0, 1) ) and ( echiquier[0][x2][y2] == "  " ) ):
                    result=True
                elif (( (abs(mouv[0]), mouv[1]) == (1, 1)) and ( echiquier[0][x2][y2] != "  " ) ): # Si (le mouvement va en diagonale et va dans le bon sens) && La case de destination contien une pi??ce.
                    result=True
                elif (mouv == (0, 2) and (y1 == (3.5+(-2.5)*facteurSens)) and (echiquier[0][x2][y2] == "  ")  ):
                    result=True
                elif ((abs(mouv[0]), mouv[1]) == (1, 0) and ( echiquier[0][x2][y2][0] == 'P')):
                    result=True
                else :
                    result=False
                
        ## V??rification de la mise en echec
        #tmp = self.echiquier
        #tmp[0][x2][y2] = tmp[0][x1][y1]
        #tmp[0][x1][y1] = [""]

        #if (result and (self.echequeAuRoi(self.couleurTour(), echiquier))):
        #    result = False
            
        return result

    def estDiagonale(self, mouv): 
        result = False
        if ( abs((mouv[0][0]-mouv[1][0])/(mouv[0][1]-mouv[1][1])) == 0.5 ): # Si (x1-x2)/(y1-y2) == 0.5
            result = True

        return result


    def estDroit(self, mouv):
        result = False
        if ( ((mouv[0][0] - mouv[1][0]) * (mouv[0][1] - mouv[1][1])) == 0): # Si ((x1 - x2) * (y1 - y2)) == 0
            result = True

        return result


    def signe(self, x):
        result = 0
        if (x > 0):
            result = 1
        elif (x < 0):
            result = -1
        return result