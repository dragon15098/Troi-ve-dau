import pygame
from project.models.map import Map
map = Map()
def print_map(map, screen, map_index, ship):
    list_player = ["../images/player/player-left.png", "../images/player/player-right.png", "../images/player/player-up.png", "../images/player/player-down.png"]
    list_map = ["../images/map/map1.png", "../images/map/map2.png", "../images/map/map3.png","../images/map/map4.png", "../images/map/map5.png", "../images/map/map5.png"]
    bg_image = pygame.image.load(list_map[map_index])
    p_image = pygame.image.load(list_player[ship])
    COLOR_WHITE = (255, 255, 255)
    SQUARE_SIZE = 40
    screen.fill(COLOR_WHITE)
    screen.blit(bg_image, (0, 0))
    screen.blit(p_image, (map.player.dic_player["x"] * SQUARE_SIZE, map.player.dic_player["y"] * SQUARE_SIZE))

def print_text_box(screen):
    text_box = pygame.image.load("../images/text_box.png")
    screen.blit(text_box, (400, 0))

def print_text(map, screen):
    dic_match = map.check_around()
    if (dic_match["gem"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label_gem = font_bat.render("Bạn đang đứng gần viên đá vô cực!", 1, (0, 0, 0))
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
    win_image = pygame.image.load("../images/story/win.png")
    screen.blit(win_image, (0, 0))

def print_lose(screen):
    lose_image = pygame.image.load("../images/story/gameover.png")
    screen.blit(lose_image, (0, 0))



