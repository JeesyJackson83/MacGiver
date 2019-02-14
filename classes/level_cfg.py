#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Class for MacGyver escape game by JJ"""

import pygame
from constant import *


class Level:
    """This class is for level design"""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def level_file(self):
        """method for use an external file to create level, line by line"""
        with open(self.file, "r") as file:
            level_structure = []
            # We look line in the file
            for line in file:
                level_line = []
                # we look sprite (letters) in each line
                for sprite in line:
                    # ignore '\n' in file
                    if sprite != '\n':
                        # add sprite to list line
                        level_line.append(sprite)
                # add line in level structure
                level_structure.append(level_line)
            # save structure created
            self.structure = level_structure

    def showme(self, window):
        """Method for show level with created file -> level_file()"""
        # #load picture
        mur = pygame.image.load(WALL).convert()
        arrivee = pygame.image.load(IMAGE_ARRIVEE).convert()

        for line, col in enumerate(self.structure):
            y = line * SPRITE_WIDTH + BANNER
            for pos, sprite in enumerate(col):
                x = pos * SPRITE_WIDTH
                if sprite == 'm':  # m = mur
                    window.blit(mur, (x, y))
                elif sprite == 'a':  # a = arrivee
                    window.blit(arrivee, (x, y))
