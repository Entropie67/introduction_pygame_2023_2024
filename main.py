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
#      La boucle de jeu       #
###############################
continuer = True
while continuer:
    # gestion des événements non clavier
    for event in pygame.event.get():
        # la croix en haut à droite
        if event.type == QUIT:
            continuer = False
    # On rafraichit à chaque tour de boucle.
    pygame.display.flip()