import pygame

from project.models.map import Map
from project.views.print_map import print_map, print_text_box, print_text

pygame.init()
map = Map()
screen = pygame.display.set_mode([700, 400])
done = False
while not done:
    dx = 0
    dy = 0
    for event in pygame.event.get():
        print("1")
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
    if (dx != 0 or dy != 0):
        [next_px, next_py] = map.player.next_position(dx, dy)
        if map.check_in_map(next_px, next_py)==True:
            map.player.move(dx, dy)
        else:
            None
    print_map(map, screen )
    print_text_box(screen)
    print_text(screen)
    pygame.display.flip()



