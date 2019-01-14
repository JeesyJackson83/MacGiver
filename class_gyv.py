"""Class for MacGyver escape game by JJ"""

import pygame
from pygame.locals import *
import random
from constant import *

class Level:
    """This class is for level design"""
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def level_file(self):
        """method for use an external file to create level, line by line"""
        with open(self.file, "r") as file:
            level_structure = []
            #We look line in the file
            for line in file:
                level_line = []
                #we look sprite (letters) in each line
                for sprite in line:
                    #ignore '\n' in fila
                    if sprite != '\n':
                        #add sprite to list line
                        level_line.append(sprite)
                #add line in level structure
                level_structure.append(level_line)
            #save structure created
            self.structure = level_structure


    def showme(self, window):
        """Method for show level with created file -> level_file()"""
        #load picture
        mur = pygame.image.load(wall).convert()
        arrivee = pygame.image.load(image_arrivee).convert()


        #Check level structure
        num_line = 0
        for line in self.structure:
            #check line in structure
            num_case = 0
            for sprite in line:
                #transform position in real pixels position
                x = num_case * sprite_width
                y = num_line * sprite_width
                if sprite == 'm':   #m = mur
                    window.blit(mur, (x,y))
                elif sprite == 'a': #a = arrivee
                    window.blit(arrivee, (x,y))
                num_case += 1
            num_line += 1



class RandomObjects:
    """The class for the items."""

    def __init__(self, img_items, level):
        """Init items."""
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.check = True
        self.img_items = pygame.image.load(img_items).convert_alpha()
        self.structure = level.structure

    def showme_item(self, window):
        """Display items in random sprites"""
        while self.check:
            self.case_x = random.randint(0, sprite_length - 1)
            # We randomize the case_x position
            self.case_y = random.randint(0, sprite_length - 1)
            # same for case_y position
            if self.structure[self.case_y][self.case_x] == '0':
                # if the randomized position is located on a free space
                self.y = self.case_y * sprite_width
                # We define/accept the position for the object
                self.x = self.case_x * sprite_width
                self.check = False
                # Once we have defined a items position, we kill the loop





class Character:
    """This Class is for character initialization and movement"""
    def __init__(self, picgyv, level):
        #Character Sprite
        self.picgyv = pygame.image.load(picgyv).convert_alpha()
        #Character case and pixel positions
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #default direction for a future use case
        self.direction = self.picgyv
        #level where Charact interact
        self.level = level

    def deplacer(self, direction):
        """Method for Character movement"""

        #move right
        if direction == 'right':
            #we don't want to be off screen
            if self.case_x < (sprite_length - 1):
                #check for free space not wall
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    #case movement
                    self.case_x += 1
                    #translation case to pixel movement
                    self.x = self.case_x * sprite_width


        #move left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_width


        #move up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_width


        #move down
        if direction == 'down':
            if self.case_y < (sprite_length - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_width

