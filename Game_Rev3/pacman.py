#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import pygame
import level001
import basicSprite
from pygame.locals import *
from helpers import *
from snakeSprite import Snake,Ghost
from pacmanModule import *	

# TODO
# > add power pills
# > add cherries etc / powerups
# > choose control of ghost / pacman



if __name__ == "__main__":
	MainWindow = PyManMain(500,575)
	MainWindow.MainLoop()
       
