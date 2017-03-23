import pygame
from views.begin_game_view import print_begin
def start_control(screen):
    index_map = 0
    screen.blit("", (0,0))
    for event in pygame.event.get():
        if pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] < 200 and event == pygame.MOUSEBUTTONDOWN:
            print_begin(screen, index_map)
        index_map += 1
