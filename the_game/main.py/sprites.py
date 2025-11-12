import pygame as pg
from pygame.sprite import Sprite

class Berserker(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 200   # pixels per second

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
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 200   # pixels per second

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
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 200   # pixels per second

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