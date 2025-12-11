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
from levels import LEVEL_MAP, draw_connections
#starts pygame module

pygame.init()

#create game window variables for us to use
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#fits the surface into the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Timer setup
game_timer = 0
time_limit = 10  # 10 seconds

#game variables for loop to operate
game_paused = False
menu_state = "main"
game_state = "idle"
initiation = 'false'
spawn_timer = 0

#define fonts for us to draw text
font = pygame.font.SysFont("arialblack", 40)
debug_font = pygame.font.SysFont("arial", 18)

#define colours
TEXT_COL = (255, 255, 255)
#allows us to open up files using os
#defines route in files
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = r"C:\Users\J.Li29\OneDrive - Bellarmine College Preparatory\Documents\computer_programming\li_reign_of_soccer\the_game\images"

#load button images
#sets where the images are loaded
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
offense_img = pygame.image.load(os.path.join(IMG_FOLDER, 'offense.png')).convert_alpha()
boss1_img = pygame.image.load(os.path.join(IMG_FOLDER, 'boss1.png')).convert_alpha()
#create button instances from the button.py module
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
offense_button = button.Button(130, 400, offense_img, 1)
#images
boss1_pos = (340, 120)
#allows us to draw text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#creates batches of groups before main loop
#defines frames and variables
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()   # create the group once
player = None
current_level = None

# Spawner variables
spawn_timer = 0
spawn_rate = 0.5  # Spawn every 0.5 seconds
spawn_x = SCREEN_WIDTH // 2  # Spawn from middle of screen
spawn_y = SCREEN_HEIGHT // 2


#main loop
run = True
while run:
  #calculate dt at start of each frame
  dt = clock.tick(60) / 1000.0   # seconds since last frame, cap at 60 FPS
  
  #fills background color
  screen.fill((52, 78, 91))
  # draw debug state info by chat
  draw_text(f"State: {game_state}  Menu: {menu_state}", debug_font, (255, 255, 0), 10, 10)

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
      player = Berserker(360, 250)
      game_state = "level_select"
    if class2_button.draw(screen):
      print("mage")
      player = Mage(360, 250)
      game_state = "level_select"
    if class3_button.draw(screen):
      print("thief")
      player = Thief(360, 250)
      game_state = "level_select"
#if game is level select then draw levels from levels.py
  if game_state == "level_select":
    draw_connections(screen, LEVEL_MAP)
    for level_node in LEVEL_MAP:
        level_node.draw(screen)
        draw_text("LEVELS", font, TEXT_COL, 320, 50)
  if game_state == "move_select":
    screen.blit(boss1_img, boss1_pos)
    


  #event handler fo us to quit instance
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      # handle level selection clicks only on mouse down
      if game_state == "level_select":
        for level_node in LEVEL_MAP:
          if level_node.is_clicked(event.pos) and level_node.unlocked:
            current_level = level_node.level_id
            # go to move_select so the player can choose moves (e.g., offense)
            game_state = "move_select"
            break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        # Pause game when space is pressed
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  if game_state == "move_select":
    if offense_button.draw(screen):
      game_state = "running"
      print("offense")
      if player is not None and player not in all_sprites:
        all_sprites.add(player)
        #all_sprites.add(Mob)
    # update & draw each frame while running
    all_sprites.update(dt)
    all_sprites.draw(screen)
  elif game_state == "running":
    # Track time for 10 second limit
    game_timer += dt
    
    # Spawn projectiles from middle
    spawn_timer += dt
    if spawn_timer >= spawn_rate:
      for direction in DIRECTIONS_8:
        projectile = Projectile(None, spawn_x, spawn_y, direction)
        all_sprites.add(projectile)
      spawn_timer = 0
    
    # Check if 10 seconds elapsed
    if game_timer >= time_limit:
      game_state = "move_select"
      game_timer = 0  # Reset timer
    
    # update & draw each frame while running
    all_sprites.update(dt)
    all_sprites.draw(screen)
    
    # Check for projectile-player collisions
    if player is not None:
      for projectile in all_sprites:
        if isinstance(projectile, Projectile):
          if projectile.rect.colliderect(player.rect):
            player.health -= projectile.damage
            projectile.kill()  # Remove projectile after hit
            print(f"Player hit! Health: {player.health}")
        if player.health <= 0:
          run = False


  pygame.display.update()

pygame.quit()


