import pygame
from models.map import Map
map = Map()
def print_map(map, screen):
    pygame.init()
    done = False
    bg_image = pygame.image.load("../images/hoa.png")
    p_image = pygame.image.load("../images/mario.png")
    gem_image = pygame.image.load("../images/box.png")
    hole_image = pygame.image.load("../images/1.jpg")
    bat_image = pygame.image.load("../images/doi.png")
    COLOR_WHITE = (255, 255, 255)
            # draw image
    SQUARE_SIZE = 40
    screen.fill(COLOR_WHITE)
    screen.blit(bg_image, (0, 0))
    screen.blit(p_image, (map.player.dic_player["x"] * SQUARE_SIZE, map.player.dic_player["y"] * SQUARE_SIZE))
    screen.blit(gem_image, (map.gem.dic_gem["x"] * SQUARE_SIZE, map.gem.dic_gem["y"] * SQUARE_SIZE))
    screen.blit(hole_image, (map.hole.list_hole[0]["x"] * SQUARE_SIZE, map.hole.list_hole[0]["y"] * SQUARE_SIZE))
    screen.blit(bat_image, (map.bat.dic_bat["x"] * SQUARE_SIZE, map.bat.dic_bat["y"] * SQUARE_SIZE))
    pygame.display.flip()

def print_text_box(screen):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        text_box = pygame.image.load("../images/text_box.png")
        screen.blit(text_box, (400, 0))
        pygame.display.flip()

