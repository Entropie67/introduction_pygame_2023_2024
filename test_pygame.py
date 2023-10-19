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
