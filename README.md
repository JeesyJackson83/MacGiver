# MacGiver
Summary
Imagine a 2D labyrinth in which MacGyver would have been locked up. The exit is watched over by a bodyguard. To distract him, you need to combine the following elements dispersed in the labyrinth:

a needle
a tube
ether


Usage
This program is a standalone

Files
main.py, main script the one to run
constant.py, place for constants 
classes/ directory for character.py, level_cfg.py, objects.py
images/ directory for image files
Level_design.txt, files for maze
requirement.txt, dependence
README.md, you're reading it!

Features
One level. The structure (departure, location of the walls, arrival), should be saved in a file to easily modify it if necessary.
MacGyver will be controlled by the directional keys on the keyboard.
The objects will be randomly distributed in the maze and will change locations if the user closes the game and raises it.
The game window will be a square of 15 sprites length.
MacGyver will have to move from square to square, with 15 squares along the window's length
It will retrieve an object simply by moving on it.
The program stops only if MacGyver has recovered all objects and found the exit from the maze. If he stupid enough to comes in front of the the guard without all the objects, he dies (according to the evolution theory).
The program will be standalone, i. e. it can be run on any computer.

