
# core game loop
# input
# update
# draw
# pyright: ignore[reportMissingImports]
import math
import random
import sys
import pygame as pg
from settings import *
from sprites import *
class Game:
   def __init__(self):
      pg.init()
      self.clock = pg.time.Clock()
      self.screen = pg.display.set_mode((WIDTH, HEIGHT))
      pg.display.set_caption("Game thats cool")
      self.playing = True
   def new(self):
      # the sprite group allows us to upate and draw sprite in grouped batches
      self.all_sprites = pg.sprite.Group()
      #instantiates Player class
      self.player = Player(self, 100, 100)
      self.mob = Mob(self, 250, 200)
      self.all_sprites.add(self.player)
      self.all_sprites.add(self.mob)
   def run(self):
      while self.playing == True:
         self.dt = self.clock.tick(FPS) / 10000
         # input
         self.events()
         # process
         self.update()
         # output
         self.draw()
      pg.quit()

   def events(self):
      for event in pg.event.get():
        if event.type == pg.QUIT:
          print("this is happening")
          self.playing = False
        if event.type == pg.MOUSEBUTTONDOWN:
           print("keep clicking twin")
   def update(self):
      self.all_sprites.update()
   def draw(self):
      self.screen.fill(GREEN)
      self.all_sprites.draw(self.screen)
      pg.display.flip()

if __name__ == "__main__":
#    creating an instance or instantiating the Game class
   g = Game()
   g.new()
   g.run()
