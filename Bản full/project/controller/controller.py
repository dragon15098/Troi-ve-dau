import pygame
from project.models.map import Map
from project.controller.game_start import start_control
from project.controller.game_play import game_play
from project.controller.game_finish import finish_control

pygame.init()
map = Map()
screen = pygame.display.set_mode([900, 600])
pygame.mixer.music.load("../sounds/lactroi.wav")
pygame.mixer.music.play(-1)
global screen_number
screen_number = 0
index_image = 0
COLOR_WHITE = (255, 255, 255)
screen.fill(COLOR_WHITE)
def play_again(screen_number):
    if screen_number == 1:
        game_play(screen)
        screen_number = 2

    if screen_number == 2:
        finish_control(screen)

out_game = False
while not out_game:
    if screen_number == 0:
        start_control(screen)
        screen_number = 1
    while True:
        play_again(screen_number)
