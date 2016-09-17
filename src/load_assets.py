import os
import pygame
from random import randint

def load_image(name):
    fullpath = os.path.join('assets', 'sprites', name)
    image = pygame.image.load(fullpath).convert()

    return image

def load_sound(name):
    fullpath = os.path.join('assets', 'sounds', name)
    sound = pygame.mixer.Sound(fullpath)

    return sound

def load_music(name):
    fullpath = os.path.join('assets', 'music', name)
    music = pygame.mixer.Sound(fullpath)

    return music

def load_font(name, size):
    fullpath = os.path.join('assets', 'fonts', name)
    font = pygame.font.Font(fullpath, size)

    return font

def generate_starfield(width, height, stars):
    # Generate a background
    # TODO: Generate more realistic star colors

    field = pygame.surface.Surface((width, height)).convert()

    for i in range(stars):
        star = pygame.rect.Rect(randint(0, width), randint(0, height), 2, 2)
        pygame.draw.rect(field, (randint(0, 255), randint(0, 255), randint(0, 255)), star)

    return field

