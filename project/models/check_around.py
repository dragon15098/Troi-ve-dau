from models.map import Map
map = Map()
def check_around(map):
    near_bat = 0
    near_hole = 0
    near_gem = 0
    for dy in range(1, -2, -1):
        for dx in range(1, -2, -1):
            temp_dic_p = {"x": map.player.dic_player["x"] - dx, "y": map.player.dic_player["y"] - dy}
            if temp_dic_p == map.bat.dic_bat:
                near_bat = 1
            for i in range(len(map.hole.list_hole)):
                if temp_dic_p == map.hole.list_hole[i]:
                    near_hole = 1
                    break
            if temp_dic_p == map.gem.dic_gem:
                near_gem = 1
    print(near_gem)
    dic_match = {"bat" : near_bat, "hole" : near_hole, "gem" : near_gem}
    return dic_match
