class Bat:
    def __init__(self):
        self.list_bat = []

    def check_match_bat(self, ax, ay, list_bat):
        for i in range (len(list_bat)):
            if (ax == list_bat[i]["x"], ay == list_bat[i]["y"]):
                return True
        return False