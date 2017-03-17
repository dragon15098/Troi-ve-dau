import pygame

from models.map import Map

map = Map()

pygame.init()
screen = pygame.display.set_mode([800, 600])
done = False
map = Map()
bg_image = pygame.image.load("images/thuy.jpg")
p_image = pygame.image.load("images/mario.png")
gem_image = pygame.image.load("images/box.png")
hole_image= pygame.image.load("images/1.jpg")
bat_image = pygame.image.load("images/doi.png")

        # draw bg
COLOR_WHITE = (255, 255, 255)

        # draw image
SQUARE_SIZE = 40

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
            else:
                    dx, dy = 0, 0

        if dx != 0 or dy != 0:
            map.move_player(dx, dy)


    screen.fill(COLOR_WHITE)
            # for y in range(self.height):
            #     for x in range(self.width):
            #         screen.blit(bg_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
    screen.blit(bg_image, (0 ,0))
    screen.blit(p_image, (map.player.dic_player["x"] * SQUARE_SIZE, map.player.dic_player["y"] * SQUARE_SIZE))
    screen.blit(gem_image, (map.gem.dic_gem["x"] * SQUARE_SIZE, map.gem.dic_gem["y"] * SQUARE_SIZE))
    screen.blit(hole_image, (map.hole.list_hole[0]["x"] * SQUARE_SIZE, map.hole.list_hole[0]["y"] * SQUARE_SIZE))
    screen.blit(bat_image, (map.bat.dic_bat[0]["x"] * SQUARE_SIZE, map.bat.dic_bat[0]["y"] * SQUARE_SIZE))
    pygame.display.flip()