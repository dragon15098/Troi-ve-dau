class Hole:
    def __init__(self):
        self.list_hole = []

    def check_match_hole(self, x, y, list_hole):
        for i in range (len(list_hole)):
            if (x == list_hole[i]["x"], y == list_hole[i]["y"]):
                return True
        return False

