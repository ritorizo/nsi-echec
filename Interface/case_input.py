import pygame
pygame.init()

def input() :
  ecran_x = 500
  ecran_y = 248 # 126
  taille_ecran = (ecran_x,ecran_y)
  marge = (ecran_x-ecran_y)/2
  taille_case = int(ecran_y/9)
  marge_gauche = marge + taille_case
  marge_haut = taille_case
  ecran = pygame.display.set_mode(taille_ecran)
  base_font = pygame.font.Font(None,32)
  user_text = ""
  input_rect = pygame.Rect(taille_case,6*taille_case,140,32)

  running = True
  while running == True :
  
  # Stopper le programme si la fenêtre est fermé.
    for event in pygame.event.get():
      if event.type == pygame.QUIT : 
        running = False
        pygame.quit()
        print("Fermeture")

      if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_BACKSPACE:
          user_text = user_text[:-1]
        else :
          user_text += event.unicode
  
    ecran.fill((0,0,0))
    
    pygame.draw.rect(ecran,(255,255,255),input_rect,2)
    text_surface = base_font.render(user_text,True,(255,255,255))
    ecran.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))

    input_rect.w = max(100,text_surface.get_width() + 10)
    pygame.display.flip()

    print(user_text)