## Import du module Pygame​

#import pygame   ## Initialisation de tous les modules Pygame​
#pygame.init()   # Initialisation de tous les modules Pygame​


#--- Création de la fenêtre de jeu ---# ​
#pygame.display.set_mode((500, 200))

#--- Lignes pour maintenir la fenêtre ouverte ...​
#running = True
#while running :
#    # --- Pour fermer la fenêtre de jeu ---#​
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    # --- Gestion du FPS ---#​
#    pygame.time.Clock().tick(60)

# --- Arrêter correctement l’exécution de Pygame ---#​
#pygame.quit()