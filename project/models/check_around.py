from project.models.map import Map
map = Map()
def check_around(map):
    near_bat = False
    near_hole = False
    near_gem = False
    for dy in range(1, -2, -1):
        for dx in range(1, -2, -1):
            temp_dic_p = {"x": map.player.dic_player["x"] - dx, "y": map.player.dic_player["y"] - dy}
            if(dx == 0) and (dy == 0):
                near_bat = False
                near_hole = False
                near_gem = False
            if temp_dic_p == map.bat.dic_bat:
                near_bat = True
            for i in range(len(map.hole.list_hole)):
                if temp_dic_p == map.hole.list_hole[i]:
                    near_hole = True
                    break
            if temp_dic_p == map.gem.dic_gem:
                near_gem == True
