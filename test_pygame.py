import pygame
from pygame.locals import *

###############################
#      Initialisation         #
###############################

# Initialisation de Pygame
pygame.init()
# création d'une fenête de 640 sur 480
fenetre = pygame.display.set_mode((640, 480))
# Titre de la fenêtre :
pygame.display.set_caption("Mon jeu")
# Initialisation d'une horloge.
# Utile pour gérer la fréquence d'images en jeu
clock = pygame.time.Clock()
# Répétition d'une touche
pygame.key.set_repeat(50, 10)

###############################
#       Le fond               #
###############################
# Un fond en couleur
VIOLET = (127, 0, 255) # Format RGB
# fill pour remplir la fenêtre de la couleur donnée.
fenetre.fill(VIOLET)
# Une image de fond
fond = pygame.image.load("images/sable.jpg").convert()
# Maintenant il faut coller l'image dans la fenêtre au coordonnées (0, 0)
fenetre.blit(fond, (0, 0))
###############################
#       Le perso              #
###############################
# On charge l'image
diana = pygame.image.load("images/Diana.png").convert_alpha()
# On change un peu la taille
diana = pygame.transform.scale(diana, (64, 64))
# On crée un rectangle de la même taille que Diana
diana_rec = diana.get_rect()
# On place ce rectangle
diana_rec.left = 200
diana_rec.top = 200
# Et enfin, on colle l'image dans le rectangle.
fenetre.blit(diana, diana_rec)
###############################
#      La boucle de jeu       #
###############################
continuer = True
while continuer:
    # gestion des événements non clavier
    for event in pygame.event.get():
        # la croix en haut à droite
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:  # appui sur une touche
            if event.key == K_RIGHT:
                print("touche Droite")
                diana_rec.left += 5
    # On rafraichit à chaque tour de boucle.
    fenetre.blit(diana, diana_rec)
    pygame.display.flip()
