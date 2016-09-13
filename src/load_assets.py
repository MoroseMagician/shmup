import os
import pygame

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

def load_font(name):
    fullpath = os.path.join('assets', 'fonts', name)
    font = pygame.font.Font(fullpath)

    return font
