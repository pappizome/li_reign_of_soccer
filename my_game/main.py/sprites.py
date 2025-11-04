import pygame as pg
from pygame.sprite import Sprite
# pyright: ignore[reportMissingImports]
from settings import *
from random import randint
#creates the player sprite
class Player(Sprite):
    #runs method when program is init
    def __init__(self, game, x, y):
        #creates Sprite upon init
        Sprite.__init__(self)
        self.game = game
        #colors sprite and positions sprite
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def update(self):
        pass
    def get_keys(self):
        #if wasd is pressed, it will move on either y or x on graph.
        #def keys as variable
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
    def update(self):
        self.get_keys()
class Mob(Sprite):
    def __init__(self, game, x, y):
        #creates Sprite upon init
        Sprite.__init__(self)
        self.game = game
        #colors sprite and positions sprite
        self.image = pg.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < WIDTH:
            self.rect.x -= self.speed
        if self.rect.x > WIDTH:
            self.rect.x += self.speed