import pygame
from pokemon import Pokemon

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pokemon = Pokemon(1, 1)

    def print_map(self):
        pygame.init()
        screen = pygame.display.set_mode([800, 600])
        done = False

        # draw bg
        COLOR_WHITE = (255, 255, 255)

        # draw image
        p_image = pygame.image.load("mario.png")
        bg_image = pygame.image.load("square.png")
        box_image = pygame.image.load("box.jpg")
        win_image = pygame.image.load("win.jpg")
        gate_image = pygame.image.load("gate.jpg")
        SQUARE_SIZE = 32

        while not done:
            # get event
            dx, dy = 0, 0
            # process game events
            # repaint
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    if event.key == pygame.K_RIGHT:
                        dx = 1
                    if event.key == pygame.K_UP:
                        dy = -1
                    if event.key == pygame.K_DOWN:
                        dy = 1
                if (dx != 1) or (dy != 1):
                    self.move_player(dx, dy)

            screen.fill(COLOR_WHITE)
            screen.blit(p_image, (self.player.x * SQUARE_SIZE, self.player.y * SQUARE_SIZE))
            screen.blit(box_image, (self.box.x * SQUARE_SIZE, self.box.y * SQUARE_SIZE))
            screen.blit(gate_image, (self.gate.x * SQUARE_SIZE, self.gate.y * SQUARE_SIZE))
            for y in range(self.height):
                for x in range(self.weight):
                    screen.blit(bg_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
            if (self.win(self.box.x, self.box.y, self.gate.x, self.gate.y)):
                screen.blit(win_image, (100, 100))
            pygame.display.flip()



