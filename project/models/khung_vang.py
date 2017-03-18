import pygame
from models.map import Map
pygame.init()

def print_text_box():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen = pygame.display.set_mode([300, 194])
        text_box = pygame.image.load("../images/text_box.png")
        screen.blit(text_box, (0, 0))
        pygame.display.flip()

print_text_box()