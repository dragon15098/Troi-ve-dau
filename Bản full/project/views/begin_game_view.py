import pygame
def print_begin(screen, index_image):
    if index_image < 5:
        list_image_start = ["../images/story/1-1.png", "../images/story/1-2.png", "../images/story/1-3.png", "../images/story/1-4.png", "../images/story/1-5.png"]
        image = pygame.image.load(list_image_start[index_image])
        screen.blit(image, (0, 0))
    pygame.display.flip()
