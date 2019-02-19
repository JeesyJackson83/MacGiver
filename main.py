#! /usr/bin/env python3
# coding: utf-8

"""
MacGyver Game by JJ
find the exit but catch the items for it before

Python Script
Files : main.py, constant.py, level_design.txt
Directory: images and classes with character.py, level_cfg.py, objects.py
"""

# python libraries
import os
import pygame
from pygame.locals import *

# personal libraries
import classes.character as chrc
import classes.level_cfg as lcfg
import classes.objects as ro
import classes.game_setting as game
import constant as cs


pygame.init()

# Open Pygame window (width = height)
window = pygame.display.set_mode((cs.COTE_FENETRE, cs.COTE_FENETRE_H))
game_set = game.Game.w_game_init()

# Main Loop
continue_main = 1
while continue_main:
    # chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(cs.START).convert()
    window.blit(accueil, (0, 30))

    # rafraichissement
    pygame.display.flip()

    # remise des variables a 1 à chaque tour de boucle
    continue_game = 1
    continue_start = 1

    # boucle d'accueil
    while continue_start:

        # 30 frames per seconds
        # pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # if user want to quit
            # All loop don't be launch
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_start = 0
                continue_game = 0
                continue_main = 0
                end_game = 0
                # variable for level choice
                begin = 0

            elif event.type == KEYDOWN:
                # start level
                if event.key == K_F1:
                    continue_start = 0
                    begin = os.path.join("level_storage/level_design_01.txt")
                # if event.key == K_F2:
                #     continue_start = 0
                #     begin = os.path.join("level_storage/level_design_02.txt")

    # check if user has made a choice
    # if not we don't load the map
    if begin != 0:
        # load background
        background = pygame.image.load(cs.BACKGROUND_P).convert()

        # level creation with level file
        level = lcfg.Level(begin)
        level.level_file()
        level.showme(window)

        # Character and objects variables
        mcgyv = chrc.Character(cs.PICGYV_P, level)
        needle = ro.RandomObjects(cs.NEEDLE_P, level)
        needle.showme_item(window)
        tube = ro.RandomObjects(cs.TUBE_P, level)
        tube.showme_item(window)
        ether = ro.RandomObjects(cs.ETHER_P, level)
        ether.showme_item(window)
        # Load syringe picture
        syringe = pygame.image.load(cs.SYRINGE_P).convert_alpha()

        # Show inventory status
        # game.Game.handle_inventory(window)
        font_inventory = pygame.font.Font(None, 30)
        inventory = font_inventory.render("Inventory: ", 1, (255, 255, 255))
        window.blit(inventory, (10, 5))

        # boolean for objects
        needle_on = True
        tube_on = True
        ether_on = True

    # Game Loop
    while continue_game:

        # 30 frames per seconds
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # if Quit close the program
            if event.type == QUIT:
                continue_game = 0
                continue_main = 0
                end_game = 0

            elif event.type == KEYDOWN:
                # if Echap return to lobby
                if event.key == K_ESCAPE:
                    continue_game = 0
                    end_game = 0

                # MacGyver move key
                elif event.key == K_RIGHT:
                    mcgyv.deplacer('right')
                elif event.key == K_LEFT:
                    mcgyv.deplacer('left')
                elif event.key == K_UP:
                    mcgyv.deplacer('up')
                elif event.key == K_DOWN:
                    mcgyv.deplacer('down')

        # refresh position
        window.blit(background, (0, 30))
        level.showme(window)
        window.blit(mcgyv.direction, (mcgyv.x, mcgyv.y))

        # boolean for interaction between Character and objects
        if needle_on:
            window.blit(needle.img_items, (needle.x, needle.y))
            if (mcgyv.x, mcgyv.y) == (needle.x, needle.y):
                # Print text on home screen
                needle_on = False
                window.blit(needle.img_items, (120, 0))

        # boolean for interaction between Character and objects
        if tube_on:
            window.blit(tube.img_items, (tube.x, tube.y))
            if (mcgyv.x, mcgyv.y) == (tube.x, tube.y):
                tube_on = False
                window.blit(tube.img_items, (150, 0))

        # boolean for interaction between Character and objects
        if ether_on:
            window.blit(ether.img_items, (ether.x, ether.y))
            if (mcgyv.x, mcgyv.y) == (ether.x, ether.y):
                ether_on = False
                window.blit(ether.img_items, (180, 0))

        incomplete_stuff = True
        if needle_on is False and tube_on is False and ether_on is False:
            incomplete_stuff = False
            window.blit(syringe, (210, 0))

        # Win condition, back to lobby
        if level.structure[mcgyv.case_y][mcgyv.case_x] == 'a' and incomplete_stuff is False:
            continue_game = 0
            end_game = 1
            win_token = True

        elif level.structure[mcgyv.case_y][mcgyv.case_x] == 'a':
            continue_game = 0
            end_game = 1
            win_token = False

        pygame.display.flip()

    while end_game:
        # Show only background
        end_status = pygame.image.load(cs.BACKGROUND_P).convert()
        window.blit(end_status, (0, 30))

        # Show key for Quit
        font_quit = pygame.font.Font(None, 30)
        quit_game = font_quit.render("Press Echap to Quit the Game", 1, (255, 255, 255))
        window.blit(quit_game, (80, 250))

        if win_token:
            # Show win message
            font_win = pygame.font.Font(None, 30)
            win_game = font_win.render("Well Done ! You're knocked him !", 1, (49, 246, 10))
            window.blit(win_game, (80, 200))

        else:
            # Show loose message
            font_loose = pygame.font.Font(None, 30)
            loose_game = font_loose.render("You missed something and death found you !", 1, (255, 0, 0))
            window.blit(loose_game, (20, 200))

        # 30 frames per seconds
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # user needs to quit
            # All loop need to stop
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_start = 0
                continue_game = 0
                continue_main = 0
                end_game = 0

        pygame.display.flip()
