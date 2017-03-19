import pygame
from project.models.map import Map
<<<<<<< HEAD
from project.views.print_map import print_map, print_text_box, print_text, print_square, print_win, print_lose,print_text_rule,print_rule
=======
from project.views.print_map import print_map, print_text_box, print_text, print_square, print_win, print_lose
>>>>>>> fc1861727a1bae8c88b9a78b621a0ca587e6b8f6

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
        if map.check_lose():
            done = True
<<<<<<< HEAD
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
        if map.check_in_map(next_px, next_py) and not map.check_win() and not map.check_lose():
            map.player.move(dx, dy)
        if map.player.dic_player == map.bat.dic_bat:
            map.player.dic_player = map.add_bat()
    print_map(map, screen)
    print_square(screen,SQUARE_SIZE,map.width,map.height)
    print_text_box(screen)
    print_text(map, screen)
    print_text_rule(screen)
    print_rule(screen)
    if map.check_lose():
        print_lose(screen)
    if map.check_win():
        map.index_map += 1
        print_win(screen)


    pygame.display.flip()



=======
            out_game = True
            print_lose(screen)
        if map.player.dic_player == map.gem.dic_gem:
            done = True
        print_map(map, screen)
        print_square(screen,SQUARE_SIZE,map.width,map.height)
        print_text_box(screen)
        print_text(map, screen)
        pygame.display.flip()
    map_index += 1
print_win(screen)
>>>>>>> fc1861727a1bae8c88b9a78b621a0ca587e6b8f6
