import pygame
pygame.init()
class Interface :
  taille_ecran = (500,248)
  screen = pygame.display.set_mode(taille_ecran)
  pygame.display.set_caption("Echecs.exe")
  BLACK = (0, 0, 0)
  BLUE = (0,0,255)
  GRAY = (128,128,128)
  RED = (255,0,0)
  def menuDemarrage(self) :

    # Définition des variables qui géreront les while, les boutons et la valeur qui sera retourné
    mode = ("x","y")
    choix_mode = False

    # Colorisation de l'écran pour l'esthétique
    self.screen.fill((207,185,151))

    # Prépration des tailles de police pour les boutons
    police = pygame.font.Font(None,25)
    police_button = pygame.font.Font(None,30)

    # Création des textes et des boutons
    titre = police.render("Bienvenue dans le jeu d'échecs des élèves de NSI", True, self.BLACK ) # (408,18)
    txt_choix_mode = police.render("Choisissez le mode de jeu :", True, self.BLACK) # (228,18)
    button_modejcr = police.render("Mode joueur contre robot ", True, self.BLUE) # (0,0,219,18)
    button_retour = police_button.render("<- Retour",True,self.RED) #(0,0,150,34)

    #Récupération des tailles des boutons
    co_button_jcr = button_modejcr.get_rect()
    co_button_retour = button_retour.get_rect()

    # Affichage des textes et des boutons
    self.screen.blit(titre,(46,0))
    self.screen.blit(txt_choix_mode,(136,20))
    self.screen.blit(button_modejcr,(145,40))
    self.screen.blit(button_retour,((400),(248-34)))
    
    # Boucle de jeu
    running = True
    while running == True :
      pygame.display.flip()

      for event in pygame.event.get():
        if event.type == pygame.QUIT : 
          running = False
          pygame.quit()
          print("Fermeture")
        
        # Récupères la position de la souris quand elle est cliquée
        if event.type == pygame.MOUSEBUTTONDOWN:
          if choix_mode == False :
            mouse_pos = event.pos
            print(mouse_pos)

            # Quand le bouton jcr est cliqué
            if mouse_pos[0] >= 145 and mouse_pos[0] <= co_button_jcr[2]+145 and mouse_pos[1] >= 40 and mouse_pos[1] <= 60 :
              print("Mode joueur contre joueur")
              mode = ("J","R")
              print(mode)
              button_modejcr = police.render("Mode joueur contre robot ", True, self.GRAY) # (0,0,219,18)
              self.screen.blit(button_modejcr,(145,40))
              choix_mode = True
              # griser quand résultat choisi + button_retour
          

interface = Interface()
interface.menuDemarrage()