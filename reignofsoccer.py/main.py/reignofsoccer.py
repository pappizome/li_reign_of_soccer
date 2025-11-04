#created by James Li with help from 



import math
import random
import sys
import pygame as pg
from settings import *
from os import path
from math import floor
from random import randint
from random import choice
vec = pg.math.Vector2
import pygame
import button
class Game:
   def __init__(self):
      pg.init()
      self.clock = pg.time.Clock()
      self.screen = pg.display.set_mode((WIDTH, HEIGHT))
      pg.display.set_caption("james gamese")
      self.playing = True

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pg.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)