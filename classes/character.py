#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Class for MacGyver escape game by JJ"""

import pygame
from pygame.locals import *
from constant import *


class Character:
    """This Class is for character initialization and movement"""

    def __init__(self, picgyv, level):
        # Character Sprite
        self.picgyv = pygame.image.load(picgyv).convert_alpha()
        # Character case and pixel positions
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 30
        # default direction for a future use case
        self.direction = self.picgyv
        # level where Charact interact
        self.level = level

    def deplacer(self, direction):
        """Method for Character movement"""

        # move right
        if direction == 'right':
            # we don't want to be off screen
            if self.case_x < (SPRITE_LENGTH - 1):
                # check for free space not wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # case movement
                    self.case_x += 1
                    # translation case to pixel movement
                    self.x = self.case_x * SPRITE_WIDTH

        # move left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_WIDTH

        # move up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_WIDTH + BANNER

        # move down
        if direction == 'down':
            if self.case_y < (SPRITE_LENGTH - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_WIDTH + BANNER
