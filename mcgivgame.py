"""
MacGyver Game by JJ
find the exit but catch the items for it before

Python Script
Files : mcgivgame.py, class.py, constant.py, level.txt + pictures
"""
import pygame
from pygame.locals import *

from class_gyv import *
from constant import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(window_title)

#boucle principale
continuer = 1
while continuer:
    #chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(start).convert()
    window.blit(accueil, (0,0))

    #rafraichissement
    pygame.display.flip()

    #remise des variables a 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #boucle d'accueil
    while continuer_accueil:

        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #si l'utilisateur quitte, on met les variables
            #de boucle a 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #variable de choix de niveau
                begin = 0

            elif event.type == KEYDOWN:
                #lancement du niveau 1
                if event.key == K_F1:
                    continuer_accueil = 0 #on quitte l'accueil
                    begin = 'level.txt' #On défini le niveau a charger



    #verif que le joueur a bie nfait un choix de niveau
    #pour ne pas charger s'il quitte
    if begin != 0:
        #chargement du fond
        background = pygame.image.load(background_p).convert()

        #génrération d'un niveau à partir d'un fichier
        level = Level(begin)
        level.level_file()
        level.showme(window)

        #creation de MacG
        mcgyv = Character("images/MacGyver.png", level)

    #Boucle du jeu
    while continuer_jeu:

        #limitation vitesse boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                #si ECHAP ici on revient quu'au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

                #touche de déplacement de DK
                elif event.key == K_RIGHT:
                    mcgyv.deplacer('right')
                elif event.key == K_LEFT:
                    mcgyv.deplacer('left')
                elif event.key == K_UP:
                    mcgyv.deplacer('up')
                elif event.key == K_DOWN:
                    mcgyv.deplacer('down')

        #affichages aux nouvelles positions
        window.blit(background, (0,0))
        level.showme(window)
        window.blit(mcgyv.direction, (mcgyv.x, mcgyv.y)) #dk.direction = l'image dan la bonne direction
        pygame.display.flip()

        #victoire -> retour a l'accueil
        if level.structure[mcgyv.case_y][mcgyv.case_x] == 'a':
            continuer_jeu = 0