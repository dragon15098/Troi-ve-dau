import random

from project.models.gem import Gem
from project.models.player import Player
from project.models.bat import Bat
from project.models.hole import Hole


class Map:
    def build_map(self, index_map):
        self.width = 4 + index_map
        self.height = 4 + index_map
        self.player = Player({"x": random.randint(0, self.width - 1), "y": random.randint(0, self.height - 1)})
        self.done_temp = False
        while not self.done_temp:
            temp_gem_x = random.randint(0, self.width - 1)
            temp_gem_y = random.randint(0, self.height - 1)
            if not (self.player.dic_player["x"] == temp_gem_x and self.player.dic_player["y"] == temp_gem_y):
                self.gem = Gem(temp_gem_x, temp_gem_y)
                self.done_temp = True
        self.hole = Hole()
        self.add_hole(self.width, self.height, index_map)
        self.bat = Bat(self.add_bat())

    def check_match(self, dic_p, temp_hole_x, temp_hole_y, list_hole, dic_gem):
        for i in range(len(list_hole)):
            if (abs(temp_hole_x - list_hole[i]["x"]) == 0) or (abs(temp_hole_y - list_hole[i]["y"]) == 0):
                return True
        if (temp_hole_x == dic_p["x"]) and (temp_hole_y == dic_p["y"]):
            return True
        if (temp_hole_x == dic_gem["x"]) and (temp_hole_y == dic_gem["y"]):
            return True
        return False

    def match(self, dic_p, temp_bat_x, temp_bat_y, list_hole, dic_gem):#tạo ra 1 vị trí mới cho bat hoặc người chơi
        for i in range(len(list_hole)):
            if (temp_bat_x == list_hole[i]["x"]) and (temp_bat_x == list_hole[i]["y"]):
                return False
        if (temp_bat_x == dic_p["x"]) and (temp_bat_y == dic_p["y"]):
            return False
        if (temp_bat_x == dic_gem["x"]) and (temp_bat_y == dic_gem["y"]):
            return False
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
        return {"x": temp_x, "y": temp_y}

    def check_in_map(self, x, y):
        if (0 <= x < self.width) and (0 <= y < self.height):
            return True
        return False

    def check_around(self):
        near_bat = 0
        near_hole = 0
        near_gem = 0
        for dy in range(-1, 2, 1):
            for dx in range(-1, 2, 1):
                temp_dic_p = {"x": self.player.dic_player["x"] - dx, "y": self.player.dic_player["y"] - dy}
                if temp_dic_p == self.bat.dic_bat:
                    near_bat = 1
                for i in range(len(self.hole.list_hole)):
                    if temp_dic_p == self.hole.list_hole[i]:
                        near_hole = 1
                        break
                if temp_dic_p == self.gem.dic_gem:
                    near_gem = 1
        dic_match = {"bat": near_bat, "hole": near_hole, "gem": near_gem}
        return dic_match

    def check_lose(self):
        for i in range(len(self.hole.list_hole)):
            if self.player.dic_player == self.hole.list_hole[i]:
                return True


