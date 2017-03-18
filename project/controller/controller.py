from models.map import Map
from models.print_map import print_map, print_text_box
import pygame
map = Map()
screen = pygame.display.set_mode([700, 400])
done = False
while not done:
    print_map(map, screen)
    print_text_box(map,screen)