import pygame
# need system to break the program
from hero import Hero
import os
from settings import Settings
from game_function import check_events;
from pygame.sprite import Group, groupcollide;
from enemy import Enemy;


game_settings = Settings()
# itit al of the pygame modules
pygame.init()
screen = pygame.display.set_mode(game_settings.screen_size)
hero = Hero(screen, game_settings)
enemies = Group();
enemies.add(Enemy(screen, game_settings));
# make a backgroung color
# put a message on the status bar so the platyer knows the name of the game
pygame.display.set_caption("Recruiter Attack!!")

# this loop will run forever...
while 1:
    check_events(hero)
    screen.fill(game_settings.bg_color)
    hero.update_me();
    hero.draw_me();

    for enemy in enemies.sprites():
        enemy.update_me(hero);
        enemy.draw_me();


    pygame.display.flip()
