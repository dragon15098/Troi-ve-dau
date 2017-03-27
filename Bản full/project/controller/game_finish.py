import sys
import pygame
from project.views.finish_game_view import print_finish
def finish_control(screen):
    pygame.init()
    done = False
    while not done:
        print_finish(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and 298 <= pygame.mouse.get_pos()[0] < 439 and 286 <= pygame.mouse.get_pos()[1] < 494:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and 494 <= pygame.mouse.get_pos()[0] < 586 and 286 <= pygame.mouse.get_pos()[1] < 494:
                sys.exit()

