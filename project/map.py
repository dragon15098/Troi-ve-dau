import pygame
from player import Player
import random
from gem import Gem
from hole import Hole
from bat import Bat

class Map:
    def __init__(self):
        self.index_map = 1
        self.width = 4 + self.index_map
        self.height = 4 + self.index_map
        self.player = Player(random.randint(0,self.width - 1), random.randint(0,self.height - 1))
        self.done_temp = False
        while not self.done_temp:
            temp_gem_x = random.randint(0, self.width - 1)
            temp_gem_y = random.randint(0, self.height - 1)
            if not (self.player.dic_player["x"] == temp_gem_x and self.player.dic_player["y"] == temp_gem_y):
                self.gem = Gem(temp_gem_x, temp_gem_y)
                self.done_temp = True
        self.hole = Hole()
        self.bat = Bat()
        self.add_hole(self.width, self.height, self.index_map)
        self.add_bat()
        print(self.player.dic_player)
        print(self.hole.list_hole)
        print(self.gem.dic_gem)
        print(self.bat.dic_bat)


    def check_match(self, dic_p, temp_hole_x, temp_hole_y, list_hole, dic_gem):
        for i in range(len(list_hole)):
            if (abs(temp_hole_x - list_hole[i]["x"]) > 2) and (abs(temp_hole_x - list_hole[i]["y"]) > 2):
                return True
        if (temp_hole_x == dic_p["x"]) and (temp_hole_y == dic_p["y"]):
            return True
        if (temp_hole_x == dic_gem["x"]) and (temp_hole_y == dic_gem["y"]):
            return True
        return False

    def match(self, dic_p, temp_bat_x, temp_bat_y, list_hole, dic_gem): #tạo ra 1 vị trí mới cho bat hoặc người chơi
        for i in range(len(list_hole)):
            if (abs(temp_bat_x == list_hole[i]["x"])) and (abs(temp_bat_x == list_hole[i]["y"])):
                return False
        if (temp_bat_x == dic_p["x"]) and (temp_bat_y == dic_p["y"]):
            return False
        if (temp_bat_x == dic_gem["x"]) and (temp_bat_y == dic_gem["y"]):
            return  False
        return True

    def add_hole(self, weidth, height, index_map): #tạo ra 1 list hole mới random vị trí
        for i in range(index_map):
            temp_x = random.randint(0, weidth - 1)
            temp_y = random.randint(0, height - 1)
            while self.check_match(self.player.dic_player, temp_x, temp_y, self.hole.list_hole, self.gem.dic_gem):
                temp_x = random.randint(0, weidth - 1)
                temp_y = random.randint(0, height - 1)
            self.hole.list_hole.append({"x": temp_x, "y": temp_y})

    def add_bat(self): #tạo ra 1 con bat không trùng các vị trí khác
        temp_x = random.randint(0, self.width - 1)
        temp_y = random.randint(0, self.height - 1)
        while not self.match(self.player.dic_player, temp_x, temp_y, self.hole.list_hole, self.gem.dic_gem):
            temp_x = random.randint(0, self.width - 1)
            temp_y = random.randint(0, self.height - 1)
        self.bat.dic_bat.append({"x": temp_x, "y": temp_y})

    def next_map(self):
        map == map + 1
    #
    # def print_map(self):
    #     pygame.init()
    #     screen = pygame.display.set_mode([800, 600])
    #     done = False
    #     bg_image = pygame.image.load("images/thuy.jpg")
    #     p_image = pygame.image.load("images/mario.png")
    #     gem_image = pygame.image.load("images/box.png")
    #     hole_image= pygame.image.load("images/1.jpg")
    #     bat_image = pygame.image.load("images/doi.png")
    #
    #     # draw bg
    #     COLOR_WHITE = (255, 255, 255)
    #
    #     # draw image
    #     SQUARE_SIZE = 40
    #
    #     while not done:
    #         dx = 0
    #         dy = 0
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 done = True
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_LEFT:
    #                     dx = -1
    #                 elif event.key == pygame.K_RIGHT:
    #                     dx = 1
    #                 elif event.key == pygame.K_UP:
    #                     dy = -1
    #                 elif event.key == pygame.K_DOWN:
    #                     dy = 1
    #                 else:
    #                     dx, dy = 0, 0
    #
    #         if dx != 0 or dy != 0:
    #             map.move_player(dx, dy)
    #
    #
    #         screen.fill(COLOR_WHITE)
    #         # for y in range(self.height):
    #         #     for x in range(self.width):
    #         #         screen.blit(bg_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
    #         screen.blit(bg_image, (0 ,0))
    #         screen.blit(p_image, (self.player.dic_player["x"] * SQUARE_SIZE, self.player.dic_player["y"] * SQUARE_SIZE))
    #         screen.blit(gem_image, (self.gem.dic_gem["x"] * SQUARE_SIZE, self.gem.dic_gem["y"] * SQUARE_SIZE))
    #         screen.blit(hole_image, (self.hole.list_hole[0]["x"] * SQUARE_SIZE, self.hole.list_hole[0]["y"] * SQUARE_SIZE))
    #         screen.blit(bat_image, (self.bat.list_bat[0]["x"] * SQUARE_SIZE, self.bat.list_bat[0]["y"] * SQUARE_SIZE))
    #         pygame.display.flip()





