import pygame

pygame.init()

# 1. Créer la fenêtre du jeu (ex: 800x600 pixels)
largeur, hauteur = 800, 600
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Fond d'écran Pygame")

# 2. Charger l'image de fond
# Optionnel : utiliser .convert() pour optimiser l'affichage
background = pygame.image.load("Exercices/lillia-and-spirit-tree-lol.3840x2160.jpg").convert()

# Optionnel : redimensionner l'image si elle n'a pas la taille de l'écran
background = pygame.transform.scale(background, (largeur, hauteur))

# Boucle principale du jeu
running = True
while running:
  # Gérer les événements (fermeture de la fenêtre, etc.)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # 3. Afficher l'image de fond aux coordonnées (0, 0)
  screen.blit(background, (0, 0))

  # Afficher les autres éléments du jeu ici...

  # 4. Actualiser l'affichage de l'écran
  pygame.display.flip()

pygame.quit()

    