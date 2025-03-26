import pygame
import os
import sys

pygame.init() #initialisation
screen = pygame.display.set_mode((800, 600)) #fenetre

image_path = os.path.join("assets","Mario", "Mario.png")#chemin d'accés sécurisé
mario = pygame.image.load(image_path) #importation mario

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Afficher l'image à la position donnée
    screen.blit(mario, (100, 100))

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()