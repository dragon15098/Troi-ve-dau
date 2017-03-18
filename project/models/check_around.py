from models.map import Map
map = Map()
def check_around(map):
    for dy in range(-1,2,1):
        for dx in range(-1,2,1):
            temp_px = map.player.dic_player["x"] - dx
            temp_py = map.player.dic_player["y"] - dy
            if(dx == 0) and (dy==0)