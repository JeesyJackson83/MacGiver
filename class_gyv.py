"""Classes du jeu de Labyrinthe Donkey Kong"""

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
            #On parcourt les lignes du ficher
            for line in file:
                level_line = []
                #on parcourr les sprites (lettres) contenus dans le fichier
                for sprite in line:
                    #on ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #on ajoute le sprite a la liste de la ligne
                        level_line.append(sprite)
                #on ajoute la ligne a la liste du niveau
                level_structure.append(level_line)
            #on save cette structure
            self.structure = level_structure


    def showme(self, window):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par level_file()"""
        #chargement des images (seule celle d'arrivée contient de la transparence)
        mur = pygame.image.load(wall).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()


        #On parcourt la liste du niveau
        num_line = 0
        # path_list = []
        for line in self.structure:
            #on parcourt les listes de lignes
            num_case = 0
            for sprite in line:
                #on calcule la position réelle en pixels
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
        #sprite du Perso
        self.picgyv = pygame.image.load(picgyv).convert_alpha()
        #position du perso en cases et pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #direction par défaut
        self.direction = self.picgyv
        #niveau dans lequel le perso se trouve
        self.level = level

    def deplacer(self, direction):
        """Méthode permettant de deplacer le perso"""

        #deplacement vers la droite
        if direction == 'right':
            #pour ne pas depasser l'ecran
            if self.case_x < (sprite_length - 1):
                #on verifie que la case de destination n'est pas un mur
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    #depalcement d'une case
                    self.case_x += 1
                    #calcul de la position "reelle" en pixel
                    self.x = self.case_x * sprite_width


        #depalcement vers la gauche
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_width


        #depalcement vers le haut
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_width


        #depalcement vers la bas
        if direction == 'down':
            if self.case_y < (sprite_length - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_width

