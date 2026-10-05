#--- Imports ---#​
import pygame   # Import du module Pygame​
import sys
import random
import math
pygame.init()   # Initialisation de tous les modules Pygame​

#--- Paramètres ---#​
# Fenêtre de jeu​
largeur = 1280
hauteur = 720
legend = "Bernard Minou"

horloge = pygame.time.Clock()

#couleur

Blanc = (250, 250, 250)

# Paramètres de texte​
affichageFont = 'comicsans' # Police d'affichage​
affichageSize = 30          # Taille d'affichage​
TextStyle = pygame.font.SysFont(affichageFont, affichageSize)


#--- Création de la fenêtre de jeu ---# ​
pygame.display.set_mode((500, 200))
#pygame.display.set_mode((largeur, hauteur))
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption(legend)

try :
    icone_surface = pygame.image.load("On se fait iech/image/miaou.png")
    pygame.display.set_icon(icone_surface)
except pygame.error :
    print("Impossible de charger l'image")

#écran titre

en_titre = True
TitreStyle = pygame.font.SysFont(affichageFont, 60)

#fond

background = pygame.image.load("On se fait iech/image/fond test.jpg").convert()
background = pygame.transform.scale(background, (largeur, hauteur))
title_screen = pygame.image.load("On se fait iech/image/title_screen.png").convert()
title_screen = pygame.transform.scale(title_screen, (largeur, hauteur))

#image

image = pygame.image.load("On se fait iech/image/chat2.png").convert_alpha()
image2 = pygame.transform.scale(image, (170, 170))
image3 = pygame.transform.scale(pygame.image.load("On se fait iech/image/chat1.png").convert_alpha(), (170, 170))
death = pygame.image.load("On se fait iech/image/chatdeath.png").convert_alpha()
death2 = pygame.transform.scale(death, (170, 170))
image4 = image2
image4 = death2 


donut = pygame.image.load("On se fait iech/image/donut.png").convert_alpha()
donut2 = pygame.transform.scale(donut, (64, 64))
brocoli = pygame.image.load("On se fait iech/image/Brocoli.png").convert_alpha()
brocoli2 = pygame.transform.scale(brocoli, (72, 72))


#music

son_recompense = pygame.mixer.Sound("On se fait iech/music/gg wp.wav")
son_gameover = pygame.mixer.Sound("On se fait iech/music/game over.wav")
son_sixseven = pygame.mixer.Sound("On se fait iech/music/six seven.mp3")
son_dix = pygame.mixer.Sound("On se fait iech/music/+10.wav")

#objet

rect = image2.get_rect()
rect.center = (300 , 300)
vitesse = 10

rect2 = donut2.get_rect()
x_rect2 = largeur
y_rect2 = random.randint(0, hauteur - 64)
rect2.center = (x_rect2, y_rect2)
vitesseDB = 1
vitesseD = vitesseDB

rect3 = brocoli2.get_rect()
x_rect3 = largeur
y_rect3 = random.randint(0, hauteur - 72)
vitesseBB = 2
vitesseB = vitesseBB

#score

score = 0
six_seven = False
dix = 0

#collision

moment_collision = 0
collision_active = False

#--- Lignes pour maintenir la fenêtre ouverte ...​
running = True
while running :
    # --- Bloc de code pour fermer la fenêtre de jeu ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if en_titre and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                en_titre = False

    # Remplissage de la fenêtre​
    #fenetre.fill(Rose)
    
    # Création de rectangles​
    

    #Déplacements

    touches = pygame.key.get_pressed()

    if not en_titre and not collision_active :
        if touches[pygame.K_q] :
            rect.x -= vitesse
        if touches[pygame.K_d] :
            rect.x += vitesse
        if touches[pygame.K_s] :
            rect.y += vitesse
        if touches[pygame.K_z] :
            rect.y -= vitesse


    #Donut

    palier = score // 10
    vitesseD = vitesseDB + palier
    x_rect2 -= vitesseD

    if x_rect2 < -64:
        x_rect2 = largeur
        y_rect2 = random.randint(0, hauteur - 64)

    rect2.x = x_rect2
    rect2.y = y_rect2



    #Brocoli

    vitesseB = vitesseDB + (palier + 2)
    x_rect3 -= vitesseB

    if x_rect3 < -72 :
        x_rect3 = largeur
        y_rect3 = random.randint(0, hauteur - 72)

    rect3.x = x_rect3
    rect3.y = y_rect3

    #Détection de proximité

    if not collision_active :
        distance = pygame.math.Vector2(rect.center).distance_to(rect2.center)

        if distance <= 200 :
            image4 = image2
        else :
            image4 = image3

    #collisions

    if rect.colliderect(rect2) and not collision_active :
        x_rect2 = largeur
        y_rect2 = random.randint(0, hauteur - 64)
        score += 1
        son_recompense.play()

    if rect.colliderect(rect3)and not collision_active :
        image4 = death2 
        son_gameover.play()
        moment_collision = pygame.time.get_ticks()
        collision_active = True

    if collision_active :
        temps_actuel = pygame.time.get_ticks()
            
        if temps_actuel - moment_collision >= 1000 : 
            en_titre = True
            collision_active = False
            

            score = 0
            rect.center = (300, 300)
            x_rect2 = 1280
            x_rect3 = 1280

    
    #scoring
    
    text_score = TextStyle.render(f"{score}", True, Blanc)

    if score % 10 == 0 and score != 0 :
        if score != dix :
            son_dix.play()
            dix = score
        

    #j'ai 4 ans

    if score == 67 and not six_seven :
        son_sixseven.play()
        six_seven = True

    
    # Affichage

    if en_titre :
        fenetre.blit(title_screen, (0, 0))
        text_title = TitreStyle.render("BERNARD MINOU", True, Blanc)
        text_instruction = TextStyle.render("Appuyez sur ESPACE pour jouer", True, Blanc)

        fenetre.blit(text_title, (400, 240))
        fenetre.blit(text_instruction, (400, 400))

    else :

        fenetre.blit(background, (0, 0)) 
        fenetre.blit(image4, rect)
        fenetre.blit(donut2, rect2)
        fenetre.blit(brocoli2, rect3)
        fenetre.blit(text_score, (50, 50))
    
    # --- Gestion du FPS ---#
    horloge.tick(60)
    # Mise à jour de l'intégralité de la surface d'affichage​
    pygame.display.flip()

pygame.quit()
sys.exit()