from models.map import Map
for i in range(100):
    map = Map()
    assert map.gem.dic_gem["x"] != map.player.dic_player["x"] or map.gem.dic_gem["y"] != map.player.dic_player["y"]

for j in range(100):
    map = Map()
    assert map.player.dic_player["x"] != map.bat.dic_bat["x"] or map.player.dic_player["y"] != map.bat.dic_bat["y"]

for x in range(100):
    map = Map()
    for i in range(len(map.hole.list_hole)):
        assert map.hole.list_hole[i]["x"] != map.gem.dic_gem["x"] or map.hole.list_hole[i]["y"] != map.gem.dic_gem["y"]