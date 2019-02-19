#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Game Class to handle all the game loop"""

import pygame
from pygame.locals import *
import constant as cs


class Game:
    """The class for the window game setting."""

    def __init__(self):
        pygame.init()

    @staticmethod
    def w_game_init():
        # Icon
        icone = pygame.image.load(cs.IMAGE_ICONE)
        pygame.display.set_icon(icone)
        # Title
        pygame.display.set_caption(cs.WINDOW_TITLE)

        # add possibility to keep key down to move
        pygame.key.set_repeat(100, 30)

        # 30 frames per seconds
        pygame.time.Clock().tick(30)

    # def handle_inventory(self):
    #     font_inventory = pygame.font.Font(None, 30)
    #     inventory = font_inventory.render("Inventory: ", 1, (255, 255, 255))
    #     window.blit(inventory, (10, 5))
