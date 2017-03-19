import pygame
from project.models.map import Map

map = Map()
def print_map(map, screen):
    bg_image = pygame.image.load("../images/hoa.png")
    p_image = pygame.image.load("../images/mario.png")
    gem_image = pygame.image.load("../images/box.png")
    hole_image = pygame.image.load("../images/1.jpg")
    bat_image = pygame.image.load("../images/doi.png")
    # rule_image = pygame.image.load("../images/rule.png")
    COLOR_WHITE = (255, 255, 255)
    SQUARE_SIZE = 40
    screen.fill(COLOR_WHITE)
    screen.blit(bg_image, (0, 0))
    screen.blit(p_image, (map.player.dic_player["x"] * SQUARE_SIZE, map.player.dic_player["y"] * SQUARE_SIZE))
    screen.blit(gem_image, (map.gem.dic_gem["x"] * SQUARE_SIZE, map.gem.dic_gem["y"] * SQUARE_SIZE))
    screen.blit(hole_image, (map.hole.list_hole[0]["x"] * SQUARE_SIZE, map.hole.list_hole[0]["y"] * SQUARE_SIZE))
    screen.blit(bat_image, (map.bat.dic_bat["x"] * SQUARE_SIZE, map.bat.dic_bat["y"] * SQUARE_SIZE))


def print_text_box(screen):
    text_box = pygame.image.load("../images/text_box.png")
    screen.blit(text_box, (map.width * 40, 0))
    pygame.display.flip()

def print_text(map, screen):
    dic_match = map.check_around()
    if (dic_match["gem"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label = font_bat.render("Gem!", 1, (0, 0, 0))
        screen.blit(label, (map.width * 40, 0))

    if (dic_match["bat"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label = font_bat.render("Bat!", 1, (0, 0, 0))
        screen.blit(label, (map.width * 40 + 50, 0))

    if (dic_match["hole"] == 1):
        font_bat = pygame.font.SysFont("monospace", 15)
        label = font_bat.render("Hole!", 1, (0, 0, 0))
        screen.blit(label, (map.width * 40 + 100, 0))

def print_square(screen, square_size, width, height):
    square = pygame.image.load("../images/square.png")
    for j in range(height):
        for i in range(width):
            screen.blit(square,(square_size*i,square_size*j))

def print_text_rule(screen):
    text_box_rule = pygame.image.load("../images/rule.png")
    screen.blit(text_box_rule, (0,200 ))
    pygame.display.flip()

def print_rule(screen):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render("ấn phím di chuyển để bắt đầu chơi !!!", 1, (0, 0, 0))
    screen.blit(label, (0, map.height * 40))

def print_win(screen):
    win_image = pygame.image.load("../images/win.png")
    screen.blit(win_image, (200, 50))

def print_lose(screen):
    lose_image = pygame.image.load("../images/lose.png")
    screen.blit(lose_image, (200, 50))



