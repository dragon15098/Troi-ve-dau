import random
import map
import play
class Hole:
    def __init__(self):
        self.list_hole = []

    def check_match(self, dic_p, temp_hole_x, temp_hole_y, list_hole):
        for i in range (len(list_hole)):
            if (abs(temp_hole_x - list_hole[i]["x"]) > 2) and (abs(temp_hole_x - list_hole[i]["y"]) > 2):
                return True
        if (temp_hole_x == dic_p["x"]) and (temp_hole_y == dic_p["y"]):
            return  True
        return False

    def add_hole(self, weidth, height):
        temp_x = random.randint(0, weidth)
        temp_y = random.randint(0, height)
        while not check_match(play.map.dic_p, temp_x, temp_y, self.list_hole):
            temp_x = random.randint(0, weidth)
            temp_y = random.randint(0, height)
        



