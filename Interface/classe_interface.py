#!/usr/bin/python
# -*- coding: latin-1 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: ascii -*-
import pygame # pip install pygame
from path import Path
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
pygame.init()
class fauxMoteur :
  coup_joueur = ()
  def coupRobot(self) :
    self.coup_joueur = (("A","5"),("B","7"))

class Interface :
  taille_ecran = (800,450)
  screen = pygame.display.set_mode(taille_ecran)
  pygame.display.set_caption("Echecs.exe")
  marge = int((taille_ecran[0]-taille_ecran[1])/2)
  taille_case = int(taille_ecran[1]/9)
  
  BLACK = (0, 0, 0)
  WHITE = (255,255,255)
  BLUE = (0,0,255)
  GRAY = (128,128,128)
  RED = (255,0,0)
  GREEN = (0,255,0)
  VIDE = (207,185,151)

  dir = Path(__file__)
  img_path = dir.abspath().dirname() / "imgs" / "CB.png"
  img_CB = pygame.image.load(img_path)
  img_CB = pygame.transform.scale(img_CB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "CN.png"
  img_CN = pygame.image.load(img_path)
  img_CN = pygame.transform.scale(img_CN,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "FB.png"
  img_FB = pygame.image.load(img_path)
  img_FB = pygame.transform.scale(img_FB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "FN.png"
  img_FN = pygame.image.load(img_path)
  img_FN = pygame.transform.scale(img_FN,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "KB.png"
  img_KB = pygame.image.load(img_path)
  img_KB = pygame.transform.scale(img_KB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "KN.png"
  img_KN = pygame.image.load(img_path)
  img_KN = pygame.transform.scale(img_KN,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "PB.png"
  img_PB = pygame.image.load(img_path)
  img_PB = pygame.transform.scale(img_PB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "PN.png"
  img_PN = pygame.image.load(img_path)
  img_PN = pygame.transform.scale(img_PN,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "QB.png"
  img_QB = pygame.image.load(img_path)
  img_QB = pygame.transform.scale(img_QB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "QN.png"
  img_QN = pygame.image.load(img_path)
  img_QN = pygame.transform.scale(img_QN,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "TB.png"
  img_TB = pygame.image.load(img_path)
  img_TB = pygame.transform.scale(img_TB,(taille_case,taille_case))
  img_path = dir.abspath().dirname() / "imgs" / "TN.png"
  img_TN = pygame.image.load(img_path)
  img_TN = pygame.transform.scale(img_TN,(taille_case,taille_case))

  echiquier = [[["TN"],["CN"],["FN"],["QN"],["KN"],["FN"],["CN"],["TN"]],[["PN"],["PN"],["PN"],["PN"],["PN"],["PN"],["PN"],["PN"]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[["PB"],["PB"],["PB"],["PB"],["PB"],["PB"],["PB"],["PB"]],[["TB"],["CB"],["FB"],["QB"],["KB"],["FB"],["CB"],["TB"]],0]
  mode = ("J","J")
  coup_joueur = ()
  etat = "rien"
  def menuDemarrage(self) :

    self.etat = "demaragge"

    # Colorisation de l'écran pour l'esthétique
    self.screen.fill(self.VIDE)

    # Prépration des tailles de police pour les boutons
    police = pygame.font.Font(None,40)
    police_button = pygame.font.Font(None,40)

    # Création des textes et des boutons
    titre = police.render("Bienvenue dans le jeu d'echecs des eleves de NSI", True, self.BLACK ) # (1369,56)
    txt_choix_mode = police.render("Choisissez le mode de jeu :", True, self.BLACK) # (752,56)
    button_modejcr = police.render("Mode joueur contre robot ", True, self.BLUE)
    button_modejcj = police.render("Mode joueur contre joueur", True, self.BLUE)
    txt_choix_couleur = police.render("Le robot doit-il commencer (joueur blanc) ?", True, self.BLACK)
    button_couleur_blanc = police.render("[Oui]",True,self.BLUE)
    button_couleur_noir = police.render("[Non]",True,self.BLUE)
    button_valider = police.render("valider ?",True,self.BLUE)
    button_retour = police_button.render("<- Retour ",True,self.RED) 

    #Récupération des tailles des textes et boutons, puis calcule leur coordonnées pour les centrer
    taille_titre = titre.get_rect() #(477,20)
    co_titre  = ((self.taille_ecran[0]-taille_titre[2])/2,0)
    
    taille_txt = txt_choix_mode.get_rect()
    co_txt = ((self.taille_ecran[0]-taille_txt[2])/2,taille_titre[3])
    
    taille_button_jcr = button_modejcr.get_rect()
    co_button_jcr = ((self.taille_ecran[0]-taille_button_jcr[2])/2,taille_titre[3]+taille_txt[3])
    
    taille_button_jcj = button_modejcj.get_rect()
    co_button_jcj = ((self.taille_ecran[0]-taille_button_jcj[2])/2,taille_titre[3]*3)

    taille_txt2 = txt_choix_couleur.get_rect()
    co_txt2 = ((self.taille_ecran[0]-taille_txt2[2]),taille_titre[3]*4)

    taille_button_blanc = button_couleur_blanc.get_rect()
    taille_button_noir = button_couleur_noir.get_rect()
    co_button_blanc = ((self.taille_ecran[0]-(taille_button_blanc[2]+taille_button_noir[2]))/2,taille_titre[3]*5)
    co_button_noir = (((self.taille_ecran[0]-(taille_button_blanc[2]+taille_button_noir[2]))/2+taille_button_blanc[2]),taille_titre[3]*5)

    taille_button_valider = button_valider.get_rect()
    co_button_valider = ((self.taille_ecran[0]-taille_button_valider[2])/2,taille_titre[3]*6)

    taille_button_retour = button_retour.get_rect()
    co_button_retour = ((self.taille_ecran[0]-taille_button_retour[2]),self.taille_ecran[1]-taille_button_retour[3])

    
    # Boucle de jeu
    running = True
    while running == True :
      pygame.display.flip()

      if self.etat == "demaragge" :
        choix_mode = False
        self.screen.fill(self.VIDE)
        button_modejcr = police.render("Mode joueur contre robot ", True, self.BLUE)
        button_modejcj = police.render("Mode joueur contre joueur", True, self.BLUE) 
        self.screen.blit(titre, co_titre)
        self.screen.blit(txt_choix_mode,co_txt)
        self.screen.blit(button_modejcr,co_button_jcr)
        self.screen.blit(button_modejcj,co_button_jcj)
        self.screen.blit(button_retour,co_button_retour)
        self.etat = "rien"

      if self.etat == "mode jcr" and choix_mode == False:
        #print("Mode joueur contre joueur")
        self.mode = ("J","R")
        #print(mode)
        button_modejcr = police.render("Mode joueur contre robot ", True, self.GREEN) 
        self.screen.blit(button_modejcr,co_button_jcr)
        button_modejcj = police.render("Mode joueur contre joueur", True, self.GRAY)
        self.screen.blit(button_modejcj,co_button_jcj)
        choix_mode = True

      if self.etat == "mode jcj" and choix_mode == False:
        #print("Mode joueur contre joueur")
        self.mode = ("J","J")
        #print(mode)
        button_modejcr = police.render("Mode joueur contre robot ", True, self.GRAY) 
        self.screen.blit(button_modejcr,co_button_jcr)
        button_modejcj = police.render("Mode joueur contre joueur", True, self.GREEN)
        self.screen.blit(button_modejcj,co_button_jcj)
        choix_mode = True

      if choix_mode == True and self.etat == "mode jcr":
        self.etat = "choix couleur"
      
      if self.etat == "choix couleur" :
        txt_choix_couleur = police.render("Le robot doit-il commencer ?", True, self.BLACK)
        button_couleur_blanc = police.render("[Oui]",True,self.BLUE)
        button_couleur_noir = police.render("[Non]",True,self.BLUE)
        self.screen.blit(txt_choix_couleur,co_txt2)
        self.screen.blit(button_couleur_blanc,co_button_blanc)
        self.screen.blit(button_couleur_noir,co_button_noir)

      if self.etat == "robot blanc" :
        txt_choix_couleur = police.render("Le robot doit-il commencer ?", True, self.BLACK)
        button_couleur_blanc = police.render("[Oui]",True,self.GREEN)
        button_couleur_noir = police.render("[Non]",True,self.GRAY)
        self.screen.blit(txt_choix_couleur,co_txt2)
        self.screen.blit(button_couleur_blanc,co_button_blanc)
        self.screen.blit(button_couleur_noir,co_button_noir)
        self.mode = ("R","J")

      if self.etat == "robot noir" :
        txt_choix_couleur = police.render("Le robot doit-il commencer ?", True, self.BLACK)
        button_couleur_blanc = police.render("[Oui]",True,self.GRAY)
        button_couleur_noir = police.render("[Non]",True,self.GREEN)
        self.screen.blit(txt_choix_couleur,co_txt2)
        self.screen.blit(button_couleur_blanc,co_button_blanc)
        self.screen.blit(button_couleur_noir,co_button_noir)
        self.mode = ("J","R")

      if self.etat == "mode jcj" or self.etat == "robot blanc" or self.etat == "robot noir" :
        choix_choisi = True
        self.screen.blit(button_valider,co_button_valider)


      for event in pygame.event.get():
        if event.type == pygame.QUIT : 
          running = False
          pygame.quit()
          print("Fermeture")
        
        # Récupères la position de la souris quand elle est cliquée
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            print(mouse_pos)

            # Quand le bouton jcr est cliqué
            if mouse_pos[0] >= co_button_jcr[0] and mouse_pos[0] <= co_button_jcr[0] + taille_button_jcr[2]  and mouse_pos[1] >= co_button_jcr[1] and mouse_pos[1] <= co_button_jcr[1] + taille_button_jcr[3] :
              self.etat = "mode jcr"

            if mouse_pos[0] >= co_button_jcj[0] and mouse_pos[0] <= co_button_jcj[0] + taille_button_jcj[2] and mouse_pos[1] >= co_button_jcj[1] and mouse_pos[1] <= co_button_jcj[1] + taille_button_jcj[3] :
              self.etat = "mode jcj"

            if mouse_pos[0] >= co_button_blanc[0] and mouse_pos[0] <= co_button_blanc[0] + taille_button_blanc[2] and mouse_pos[1] >= co_button_blanc[1] and mouse_pos[1] <= co_button_blanc[1] + taille_button_blanc[3] and self.etat == "choix couleur" :
              self.etat = "robot blanc"

            if mouse_pos[0] >= co_button_noir[0] and mouse_pos[0] <= co_button_noir[0] + taille_button_noir[2] and mouse_pos[1] >= co_button_noir[1] and mouse_pos[1] <= co_button_blanc[1] + taille_button_noir[3] and self.etat == "choix couleur" :
              self.etat = "robot noir"

            if mouse_pos[0] >= co_button_valider[0] and mouse_pos[0] <= co_button_valider[0] + taille_button_valider[2] and mouse_pos[1] >= co_button_valider[1] and mouse_pos[1] <= co_button_valider[1] + taille_button_valider[3] and choix_choisi == True :
              return self.mode
              print("fin")
              running = False

            if mouse_pos[0] >= co_button_retour[0] and mouse_pos[0] <= self.taille_ecran[0] and mouse_pos[1] >= co_button_retour[1] and mouse_pos[1] <= self.taille_ecran[1] :
              self.etat = "demaragge"
              #print("retour")

  def generationEchiquier(self) :

    self.screen.fill(self.VIDE)
    blanc = True
    gene_case = False
    gene_pion = False
    gene_co = False
    co_lettres = ["A","B","C","D","E","F","G","H"]
    co_chiffres = ["1","2","3","4","5","6","7","8"]
    police = pygame.font.Font(None,self.taille_case)

    if gene_case == False :
      for y in range(8) :
        for x in range(8) :
          if blanc == True : 
            pygame.draw.rect(self.screen,self.WHITE,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            blanc = False
          elif blanc == False:
            pygame.draw.rect(self.screen,self.BLACK,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            blanc = True
          if x == 7:
            if blanc == True:
              blanc = False
            elif blanc == False :
              blanc = True
    gene_case = True
    if gene_pion == False :
      for y in range(8) :
        for x in range(8) :
          pion_candidat = self.echiquier[y][x]
          if len(pion_candidat) >= 1 :
            pion_candidat = pion_candidat[0]
            if pion_candidat == "CB" :
              self.screen.blit(self.img_CB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "CN" :
              self.screen.blit(self.img_CN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "FB" :
              self.screen.blit(self.img_FB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "FN" :
              self.screen.blit(self.img_FN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "KB" :
              self.screen.blit(self.img_KB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "KN" :
              self.screen.blit(self.img_KN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "PB" :
              self.screen.blit(self.img_PB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "PN" :
              self.screen.blit(self.img_PN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "QB" :
              self.screen.blit(self.img_QB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "QN" :
              self.screen.blit(self.img_QN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "TB" :
              self.screen.blit(self.img_TB,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
            if pion_candidat == "TN" :
              self.screen.blit(self.img_TN,[self.marge+self.taille_case+(self.taille_case*x),self.taille_case+(self.taille_case*y),self.taille_case,self.taille_case])
    gene_pion = True
    if gene_co == False :
      for x in range(8) :
        co = police.render(co_chiffres[x], True, self.BLACK )
        self.screen.blit(co,(self.marge,(self.taille_ecran[1]-(self.taille_case+(self.taille_case*x))+10)))
      for x in range(8) :
        co = police.render(co_lettres[x],True,self.BLACK)
        self.screen.blit(co,(((self.marge+self.taille_case)+self.taille_case*x+10),10))
    gene_co = False

  def partieFini(self,etat_partie) :
    police = pygame.font.Font(None,40)

    text_fin = police.render("Partie terminee",True,self.BLACK)
    texte_vic_noir = police.render("Le joueur noir a gagne",True,self.BLACK)
    texte_vic_blanc = police.render("Le joueur blanc a gagne",True,self.BLACK)

    taille_tf = text_fin.get_rect()
    co_tf = ((self.taille_ecran[0]-taille_tf[2])/2,(self.taille_ecran[1]-taille_tf[3]*2)/2)

    taille_tvn = texte_vic_noir.get_rect()
    co_tvn = ((self.taille_ecran[0]-taille_tvn[2])/2,(self.taille_ecran[1]-taille_tvn[3]*2)/2+taille_tvn[3])

    taille_tvb = texte_vic_blanc.get_rect()
    co_tvb = ((self.taille_ecran[0]-taille_tvb[2])/2,(self.taille_ecran[1]-taille_tvb[3]*2)/2+taille_tvb[3])

    
    if etat_partie == "Blancaperdu" or etat_partie == "Noiraperdu" :
      print(etat_partie)
      self.screen.fill(self.GRAY)
      #print("La partie est terminé")
      if etat_partie == "Blancaperdu" :
        self.etat = "Noir_victoire"
      if etat_partie == "Noiraperdu" :
        self.etat = "Blanc_victoire"

      print(self.etat)
      if self.etat == "Noir_victoire" :
        self.screen.blit(text_fin,co_tf)
        self.screen.blit(texte_vic_noir,co_tvn)

      if self.etat == "Blanc_victoire" :
        self.screen.blit(text_fin,co_tf)
        self.screen.blit(texte_vic_blanc,co_tvb)

  def appelerRobot(self,coup_robot) :
    if self.mode[self.echiquier[8]%2] == "R" :
      return coup_robot

  def demanderCoup(self) :
    if self.mode[self.echiquier[8]%2] == "J" :
      ROOT = tk.Tk()
      ROOT.withdraw()
      self.coup_joueur = simpledialog.askstring(title="Echecs.exe",
                                  prompt="Entrez votre mouvement")
      print(self.coup_joueur)
      return self.coup_joueur
      
  def messageErreur(self,verifierCoup) :
    if verifierCoup == False :
      messagebox.showinfo("Echecs.exe", "Erreur : votre coup est invalide")

  def mouvement(self,coup_joueur) :
    # ((3,4),(5,2))
    self.echiquier[coup_joueur[1][1]][coup_joueur[1][0]] = self.echiquier[coup_joueur[0][1]][coup_joueur[0][0]]
    self.echiquier[coup_joueur[0][1]][coup_joueur[0][0]] = []

      

 
    


test_fini = False          
interface = Interface()
#print(interface.menuDemarrage())
running = True
while running == True :
  pygame.display.flip()
  interface.generationEchiquier()
  if test_fini == False :
    interface.mouvement(((0,7),(0,0)))
    #partie = input("test : ")
    #interface.partieFini(partie)
    test_fini = True

  for event in pygame.event.get():
        if event.type == pygame.QUIT : 
          running = False
          pygame.quit()
          print("Fermeture")

#interface.demanderCoup()
#interface.messageErreur(False)