import pygame
from random import randint
        
def generate_starfield(width, height, stars):
    # Generate a background

    field = pygame.surface.Surface((width, height)).convert()

    for i in range(stars):
        star = pygame.rect.Rect(randint(0, width), randint(0, height), 2, 2)
        pygame.draw.rect(field, (randint(0, 255), randint(0, 255), randint(0, 255)), star)

    return field

