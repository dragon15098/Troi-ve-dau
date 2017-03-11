import pygame
screen = pygame.display.set_mode([800, 600])
COLOR_WHITE = (255, 255, 255)
screen.fill(COLOR_WHITE)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(5):
        for x in range(5):
            screen.blit(pygame.image.load("bg_image.png"), (5, 5))
    screen.blit(pygame.image.load("box.jpg"), (5, 5))
    pygame.display.flip()