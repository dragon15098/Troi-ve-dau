from models.map import Map
from models.print_map import print_map, print_text_box
import pygame
pygame.init()
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
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
        if (dx != 0 or dy != 0):
            if map.check_in_map():
                map.move_player(dx, dy)
            else:
                None
    print_map(map, screen )
    print_text_box(screen)
    pygame.display.flip()



