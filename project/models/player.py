class Player:
    def __init__(self, new_dic_player):
        self.dic_player = new_dic_player

    def move(self,dx,dy):
        self.dic_player["x"] += dx
        self.dic_player["y"] += dy

    def next_position(self, dx, dy):
        return [self.dic_player["x"]+dx, self.dic_player["y"]+dy]




