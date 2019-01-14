#! /usr/bin/env python3
# coding: utf-8

"""
MacGyver Game by JJ
find the exit but catch the items for it before

Python Script
Files : mcgivgame.py, class.py, constant.py, level.txt + pictures
"""
import pygame
from pygame.locals import *
import random

from class_gyv import *
from constant import *

pygame.init()

#Open Pygame window (width = height)
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icon
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Title
pygame.display.set_caption(window_title)

#Main Loop
continue_main = 1
while continue_main:
    #chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(start).convert()
    window.blit(accueil, (0,0))

    #rafraichissement
    pygame.display.flip()

    #remise des variables a 1 à chaque tour de boucle
    continue_game = 1
    continue_start = 1

    #boucle d'accueil
    while continue_start:

        # 30 frames per seconds
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # if user want to quit
            #All loop don't be launch
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_start = 0
                continue_game = 0
                continue_main = 0
                #variable for level choice
                begin = 0

            elif event.type == KEYDOWN:
                #start level
                if event.key == K_F1:
                    continue_start = 0
                    begin = 'level.txt'



    #check if user has made a choice
    #if not we don't load the map
    if begin != 0:
        #load background
        background = pygame.image.load(background_p).convert()

        #level creation with level file
        level = Level(begin)
        level.level_file()
        level.showme(window)

        #Character and objects variables
        mcgyv = Character("images/MacGyver.png", level)
        needle = RandomObjects(needle_p, level)
        needle.showme_item(window)
        tube = RandomObjects(tube_p, level)
        tube.showme_item(window)
        ether = RandomObjects(ether_p, level)
        ether.showme_item(window)

        #boolean for objects
        needle_on = True
        tube_on = True
        ether_on = True

    #Game Loop
    while continue_game:

        # 30 frames per seconds
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # if Quit close the program
            if event.type == QUIT:
                continue_game = 0
                continue_main = 0

            elif event.type == KEYDOWN:
                #if Echap return to lobby
                if event.key == K_ESCAPE:
                    continue_game = 0

                #MacGyver move key
                elif event.key == K_RIGHT:
                    mcgyv.deplacer('right')
                elif event.key == K_LEFT:
                    mcgyv.deplacer('left')
                elif event.key == K_UP:
                    mcgyv.deplacer('up')
                elif event.key == K_DOWN:
                    mcgyv.deplacer('down')

        #refresh position
        window.blit(background, (0,0))
        level.showme(window)
        window.blit(mcgyv.direction, (mcgyv.x, mcgyv.y))

        #boolean for interaction between Character and objects
        if needle_on:
            window.blit(needle.img_items, (needle.x, needle.y))
            if (mcgyv.x, mcgyv.y) == (needle.x, needle.y):
                needle_on = False
                print("you picked Needle !")

        # boolean for interaction between Character and objects
        if tube_on:
            window.blit(tube.img_items, (tube.x, tube.y))
            if (mcgyv.x, mcgyv.y) == (tube.x, tube.y):
                tube_on = False
                print("you picked Tube !")

        # boolean for interaction between Character and objects
        if ether_on:
            window.blit(ether.img_items, (ether.x, ether.y))
            if (mcgyv.x, mcgyv.y) == (ether.x, ether.y):
                ether_on = False
                print("you picked Ether !")

        pygame.display.flip()

        incomplete_stuff = True
        if needle_on == False and tube_on == False and ether_on == False:
            incomplete_stuff = False
            print("You have all the stuff for take ground the gardian")


        #Win condition, back to lobby
        if level.structure[mcgyv.case_y][mcgyv.case_x] == 'a' and incomplete_stuff == False:
            print("Well done bro'")
            continue_game = 0
        elif level.structure[mcgyv.case_y][mcgyv.case_x] == 'a':
            print("Oops, try again !")
            continue_game = 0

