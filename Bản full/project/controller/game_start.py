import sys
import pygame
from project.views.begin_game_view import print_begin
def start_control(screen):
    pygame.init()
    index_image = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                index_image += 1
        print_begin(screen, index_image)
        if index_image == 5:
            done = True
