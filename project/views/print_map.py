import pygame
from models.map import Map
map = Map()
def print_map(map, screen, map_index):
    list_map = ["../images/map1.png", "../images/map2_1.jpg", "../images/map3.png","../images/map4.png", "../images/map5.png","../images/map5.png"]
    bg_image = pygame.image.load(list_map[map_index])
    p_image = pygame.image.load("../images/ship.png")
    gem_image = pygame.image.load("../images/box.png")
    hole_image = pygame.image.load("../images/mario.png")
    bat_image = pygame.image.load("../images/doi.png")
    # rule_image = pygame.image.load("../images/rule.png")
    COLOR_WHITE = (255, 255, 255)
    SQUARE_SIZE = 40
    screen.fill(COLOR_WHITE)
    screen.blit(bg_image, (0, 0))
    screen.blit(p_image, (map.player.dic_player["x"] * SQUARE_SIZE, map.player.dic_player["y"] * SQUARE_SIZE))
    screen.blit(gem_image, (map.gem.dic_gem["x"] * SQUARE_SIZE, map.gem.dic_gem["y"] * SQUARE_SIZE))
    for i in range (len(map.hole.list_hole)):
        screen.blit(hole_image, (map.hole.list_hole[i]["x"] * SQUARE_SIZE, map.hole.list_hole[i]["y"] * SQUARE_SIZE))
    screen.blit(bat_image, (map.bat.dic_bat["x"] * SQUARE_SIZE, map.bat.dic_bat["y"] * SQUARE_SIZE))

def print_text_box(screen):
    text_box = pygame.image.load("../images/text_box.png")
    screen.blit(text_box, (400, 0))
    text_box_rule = pygame.image.load("../images/rule.png")
    screen.blit(text_box_rule, (0, 370))

def print_text(map, screen):
    dic_match = map.check_around()
    if (dic_match["gem"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label_gem = font_bat.render("Bạn đang đứng gần viên ngọc!", 1, (0, 0, 0))
        screen.blit(label_gem, (420, 50))

    if (dic_match["bat"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label_bat = font_bat.render("Bạn đang đứng gần cổng dịch chuyển!", 1, (0, 0, 0))
        screen.blit(label_bat, (420, 100))

    if (dic_match["hole"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label_hole = font_bat.render("Bạn đang đứng gần hố đen!", 1, (0, 0, 0))
        screen.blit(label_hole, (420, 150))

def print_square(screen, square_size, width, height):
    square = pygame.image.load("../images/square.png")
    for j in range(height):
        for i in range(width):
            screen.blit(square,(square_size*i,square_size*j))

def print_win(screen):
    win_image = pygame.image.load("../images/win.png")
    screen.blit(win_image, (0, 0))

def print_lose(screen):
    lose_image = pygame.image.load("../images/lose.png")
    screen.blit(lose_image, (0, 0))



