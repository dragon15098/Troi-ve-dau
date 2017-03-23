import pygame
from models.map import Map
from controller.begin_game_control import start_control
from controller.game_play import game_play

pygame.init()
map = Map()
screen = pygame.display.set_mode([1000, 800])
pygame.mixer.music.load("../sounds/lactroi.wav")
pygame.mixer.music.play(-1)
screen_number = 0
finish_game = False
while not finish_game:
    if screen_number == 0:
        start_control(screen)
    if screen_number == 1:
        game_play(screen)
    if screen_number == 2:
