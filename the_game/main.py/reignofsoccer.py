#created by James Li with help from chat and vids

#decided to restart code from start

import pygame
import pygame as pg
#button module allows us to click onto the png we load from dirname
import button
import os
from sprites import *
from sprites import Berserker
from sprites import Mage
from sprites import Thief
from sprites import Sword
from levels import LEVEL_MAP, draw_connections
#starts pygame module

pygame.init()

#create game window variables for us to use
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#fits the surface into the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables for loop to operate
game_paused = False
menu_state = "main"
game_state = "idle"

#define fonts for us to draw text
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)
#allows us to open up files using os
#defines route in files
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = r"C:\Users\J.Li29\OneDrive - Bellarmine College Preparatory\Documents\computer_programming\li_reign_of_soccer\the_game\images"

#load button images
resume_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_resume.png')).convert_alpha()
options_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_options.png')).convert_alpha()
quit_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_quit.png')).convert_alpha()
video_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_video.png')).convert_alpha()
audio_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_audio.png')).convert_alpha()
keys_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_keys.png')).convert_alpha()
back_img = pygame.image.load(os.path.join(IMG_FOLDER, 'button_back.png')).convert_alpha()
class1_img = pygame.image.load(os.path.join(IMG_FOLDER, 'class1.png')).convert_alpha()
class2_img = pygame.image.load(os.path.join(IMG_FOLDER, 'class2.png')).convert_alpha()
class3_img = pygame.image.load(os.path.join(IMG_FOLDER, 'class3.png')).convert_alpha()
#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
class1_button = button.Button(100, 300, class1_img, 1)
class2_button = button.Button(390, 300, class2_img, 1)
class3_button = button.Button(620, 250, class3_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#creates batches of groups before main loop
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()   # create the group once
player = None
current_level = None

#game loop
run = True
while run:
  #calculate dt at start of each frame
  dt = clock.tick(60) / 1000.0   # seconds since last frame, cap at 60 FPS
  
  #fills background color
  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  if game_state == "idle":
    draw_text("Choose a CHARACTER", font, TEXT_COL, 150, 50)
    # Only draw class buttons in idle state
    if class1_button.draw(screen):
      print("berserker")
      player = Berserker(100, 100)
      all_sprites.add(player)
      game_state = "level_select"
    if class2_button.draw(screen):
      print("mage")
      player = Mage(100, 100)
      all_sprites.add(player)
      game_state = "level_select"
    if class3_button.draw(screen):
      print("thief")
      player = Thief(100, 100)
      all_sprites.add(player)
      game_state = "level_select"
      

  if game_state == "level_select":
    draw_connections(screen, LEVEL_MAP)
    for level_node in LEVEL_MAP:
        level_node.draw(screen)
        draw_text("LEVELS", font, TEXT_COL, 320, 50)
  elif game_state == "running":
    # update & draw each frame while running
    all_sprites.update(dt)
    all_sprites.draw(screen)


  #event handler fo us to quit instance
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Spawn sword at player position during gameplay
      if game_state == "running" and player is not None:
        sword = Sword(player.rect.centerx, player.rect.centery)
        all_sprites.add(sword)
      # handle level selection clicks only on mouse down
      if game_state == "level_select":
        for level_node in LEVEL_MAP:
          if level_node.is_clicked(event.pos) and level_node.unlocked:
            current_level = level_node.level_id
            game_state = "running"
            break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
      # Alternative: spawn sword on key press (e.g., 'F' key)
      if event.key == pygame.K_f and game_state == "running" and player is not None:
        sword = Sword(player.rect.centerx, player.rect.centery)
        all_sprites.add(sword)
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()


