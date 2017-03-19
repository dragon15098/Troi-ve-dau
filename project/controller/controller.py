import pygame
from models.map import Map
from views.print_map import print_map, print_text_box, print_text, print_square, print_win, print_lose,print_rule
import time
pygame.init()
map = Map()
screen = pygame.display.set_mode([1000, 1000])
SQUARE_SIZE = 40
out_game = False
map_index = 1
while map_index != 6 and not out_game:
    map.build_map(map_index)
    done = False
    while not done:
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                out_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
        if dx != 0 or dy != 0:
            [next_px, next_py] = map.player.next_position(dx, dy)
            if map.check_in_map(next_px, next_py) and not map.check_lose():
                map.player.move(dx, dy)
            if map.player.dic_player == map.bat.dic_bat:
                map.player.dic_player = map.add_bat()
        if map.player.dic_player == map.gem.dic_gem:
            done = True
            map_index += 1
        print_map(map, screen, map_index - 1)
        print_square(screen,SQUARE_SIZE,map.width,map.height)
        print_text_box(screen)
        if map.check_around():
            print_text(map, screen)
        print_rule(screen)
        if map.check_lose():
            done = True
            out_game = True
            print_lose(screen)
            pygame.display.flip()
            time.sleep(2)
        pygame.display.flip()
if map_index == 6:
    print_win(screen)
    pygame.display.flip()
    time.sleep(2)

