import pygame
from player import Player
import random
from gem import Gem

class Map:
    def check_match(self, dic_hole, ):
        if
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(random.randint(0,self.width - 1), random.randint(0,self.height - 1))
        self.gem = Gem(random.randint(0,self.width - 1), random.randint(0,self.height - 1))
        self.dic_hole = []

    def print_map(self):
        pygame.init()
        print(self.gem.gem_x, "    " , self.gem.gem_y)
        screen = pygame.display.set_mode([800, 600])
        done = False
        bg_image = pygame.image.load("bg_image.png")
        p_image = pygame.image.load("box.jpg")
        # draw bg
        COLOR_WHITE = (255, 255, 255)

        # draw image
        SQUARE_SIZE = 32

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill(COLOR_WHITE)
            for y in range(self.height):
                for x in range(self.width):
                    screen.blit(bg_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
            screen.blit(p_image, (self.player.pox* SQUARE_SIZE, self.player.poy * SQUARE_SIZE))
            pygame.display.flip()





