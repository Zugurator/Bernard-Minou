#--- Imports ---#​
import pygame   # Import du module Pygame​
pygame.init()   # Initialisation de tous les modules Pygame​

#--- Paramètres ---#​
# Fenêtre de jeu​
largeur = 500
hauteur = 200
legend = "Mes tests pygame"

###### ---------------- Pygame exercice 2 ---------------- ######
# Rectangles​
# Modifier les valeurs pour résoudre l'exercice
Rect1_X = 0 # ???
Rect1_Y = 0 # ???
Rect1_Larg = 10 # ??? 
Rect1_Haut = 10 # ???
###### --------------------------------------------------- ######

# Couleurs​
Noir = (0, 0, 0)
Blanc = (255, 255, 255)
Rouge = (255, 0, 0)
Vert = (0, 255, 0) 
Bleu = (0, 0, 255)
Jaune = (255, 255, 0) 
Cyan = (0, 255, 255) 
Magenta = (255, 0, 255)
Orange = (255, 192, 0)

#--- Création de la fenêtre de jeu ---# ​
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption(legend)

#--- Lignes pour maintenir la fenêtre ouverte ...​
running = True
while running :
    # --- Bloc de code pour fermer la fenêtre de jeu ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplissage de la fenêtre​
    fenetre.fill(Blanc)

    # Création de rectangles​
    Rect1 = pygame.draw.rect(fenetre, Rouge, (Rect1_X, Rect1_Y, Rect1_Larg, Rect1_Haut))

    # --- Gestion du FPS ---#
    pygame.time.Clock().tick(60)
    # Mise à jour de l'intégralité de la surface d'affichage​
    pygame.display.flip()

pygame.quit()