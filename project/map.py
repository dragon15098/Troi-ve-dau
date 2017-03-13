import pygame
from player import Player
import random
from gem import Gem
from hole import Hole

class Map:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.player = Player(random.randint(0,self.width - 1), random.randint(0,self.height - 1))
        self.done_temp = False
        while not self.done_temp:
            temp_gem_x = random.randint(0, self.width - 1)
            temp_gem_y = random.randint(0, self.height - 1)
            if not (self.player.dic_player["x"] == temp_gem_x and self.player.dic_player["y"] == temp_gem_y):
                self.gem = Gem(temp_gem_x, temp_gem_y)
                self.done_temp = True
        self.index_map = 1
        self.hole = Hole()
        self.add_hole(self.width, self.height, self.index_map)
        print("hole")
        print(self.hole.list_hole)
        print("player")
        print(self.player.dic_player)
        print("gem")
        print(self.gem.dic_gem)

    def check_match(self, dic_p, temp_hole_x, temp_hole_y, list_hole):
        for i in range(len(list_hole)):
            if (abs(temp_hole_x - list_hole[i]["x"]) > 2) and (abs(temp_hole_x - list_hole[i]["y"]) > 2):
                print("1")
                return True
        if (temp_hole_x == dic_p["x"]) and (temp_hole_y == dic_p["y"]):
            print("2")
            return True
        return False

    def add_hole(self, weidth, height, index_map):
        for i in range(index_map):
            temp_x = random.randint(0, weidth - 1)
            temp_y = random.randint(0, height - 1)
            while self.check_match(self.player.dic_player, temp_x, temp_y, self.hole.list_hole):
                temp_x = random.randint(0, weidth - 1)
                temp_y = random.randint(0, height - 1)
            self.hole.list_hole.append({"x": temp_x, "y": temp_y})



    def print_map(self):
        pygame.init()
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





