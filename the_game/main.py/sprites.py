import pygame as pg
from pygame.sprite import Sprite
import math
#from utils import *
WIDTH = 800
HEIGHT = 600

class Berserker(Sprite):
    def __init__(self, x, y, damage=20, health=150):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 150   # pixels per second
        self.damage = damage
        self.health = health


    def get_keys(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pg.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed * dt
        if keys[pg.K_d]:
            self.rect.x += self.speed * dt

    def update(self, dt):
        self.get_keys(dt)

class Mage(Sprite):
    def __init__(self, x, y, damage= 15, health=100):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 200   # pixels per second
        self.damage = damage
        self.health = health

    def get_keys(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pg.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed * dt
        if keys[pg.K_d]:
            self.rect.x += self.speed * dt

    def update(self, dt):
        self.get_keys(dt)
class Thief(Sprite):
    def __init__(self, x, y, damage=10, health=90):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 350   # pixels per second
        self.damage = damage
        self.health = health


    def get_keys(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pg.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed * dt
        if keys[pg.K_d]:
            self.rect.x += self.speed * dt

    def update(self, dt):
        self.get_keys(dt)

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
            self.kill()
class Projectile(Sprite):
    def __init__(self, game, x, y, direction_vec, damage=10):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((8, 8))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 250
        self.damage = damage
        
        # Normalize direction vector
        #this one line made by ai to help calculate length of vec
        length = math.sqrt(direction_vec[0]**2 + direction_vec[1]**2)
        #makes the projectile move smoothly
        if length > 0:
            self.vx = (direction_vec[0] / length) * self.speed
            self.vy = (direction_vec[1] / length) * self.speed
            #if no direction then speed is 0
        else:
            self.vx = 0
            self.vy = 0
    #moves the projectile by multiplying velocity by dt
    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        
        # remove if off-screen
        if self.rect.right < 0 or self.rect.left > WIDTH or \
           self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# 8 directions pattern
DIRECTIONS_8 = [
    (1, 0),      # right
    (1, -1),     # up-right
    (0, -1),     # up
    (-1, -1),    # up-left
    (-1, 0),     # left
    (-1, 1),     # down-left
    (0, 1),      # down
    (1, 1)       # down-right
]



