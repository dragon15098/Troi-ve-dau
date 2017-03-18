from models.map import Map
from models.print_map import print_map, print_text_box
import pygame
map = Map()
screen = pygame.display.set_mode([700, 400])
done = False
while not done:
    for event in pygame.event.get():
        print("1")
        if event.type == pygame.QUIT:
            done = True
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print_map("2")
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
        if (dx != 0 or dy != 0):
            map.move_player(dx, dy)
    print_map(map, screen)
    print_text_box(screen)


def check_inside(map, dx, dy):
    temp_px = map.player.dic_player["x"] + dx
    temp_py = map.player.dic_player["y"] + dy
    if 0 <= temp_py < map.width and 0 <= temp_py < map.height:
        return True
    return False

def move_player(map, dx, dy):
    if not map.check_inside():
        None
    else:
        map.player.dic_player["x"] += dx
        map.player.dic_player["y"] += dy
