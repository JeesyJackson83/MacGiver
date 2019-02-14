#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Class for MacGyver escape game by JJ"""

import pygame
import random
from constant import *


class RandomObjects:
    """The class for the items."""

    def __init__(self, img_items, level):
        """Init items."""
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 30
        self.level = level
        self.check = True
        self.img_items = pygame.image.load(img_items).convert()
        self.structure = level.structure

    def showme_item(self, window):
        """Display items in random sprites"""
        while self.check:
            self.case_x = random.randint(0, SPRITE_LENGTH - 1)
            # We randomize the case_x position
            self.case_y = random.randint(0, SPRITE_LENGTH - 1)
            # same for case_y position
            if self.structure[self.case_y][self.case_x] == '0':
                # if the randomized position is located on a free space
                self.y = self.case_y * SPRITE_WIDTH + BANNER
                # We define/accept the position for the object
                self.x = self.case_x * SPRITE_WIDTH
                self.check = False
                # Once we have defined a items position, we kill the loop
