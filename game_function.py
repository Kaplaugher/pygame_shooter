
# file for all game functions
import pygame;
import sys;
from hero import Hero




def check_events(hero):
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          # check for keypress
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                  hero.moving_right = True
              elif event.key == pygame.K_LEFT:
                  hero.moving_left = True
              elif event.key == pygame.K_UP:
                  hero.moving_up = True
              elif event.key == pygame.K_DOWN:
                  hero.moving_down = True
          elif event.type == pygame.KEYUP:
              if event.key == pygame.K_RIGHT:
                  hero.moving_right = False
              elif event.key == pygame.K_LEFT:
                  hero.moving_left = False
              elif event.key == pygame.K_UP:
                  hero.moving_up = False
              elif event.key == pygame.K_DOWN:
                  hero.moving_down = False
