import os
import sys
import ship
import pygame
import load_assets
from random import randint
from starfield import generate_starfield

def keyCheck(ship, keys, mods, speed = 2):
    
    if mods & pygame.KMOD_LSHIFT:
        speed = 1

    if keys[pygame.K_UP] and ship.rect.y > 0:
        ship.move_up(speed)
    if keys[pygame.K_DOWN] and ship.rect.y + ship.rect.height < height:
        ship.move_down(speed)
    if keys[pygame.K_LEFT] and ship.rect.x > 0:
        ship.move_left(speed)
    if keys[pygame.K_RIGHT] and ship.rect.x + ship.rect.width < width:
        ship.move_right(speed)

    if keys[pygame.K_z]:
        ship.shoot()

    if keys[pygame.K_e]:
        ship.explode()

    if keys[pygame.K_ESCAPE]:
        sys.exit()
pygame.init()

# 224x288 is the original arcade resolution for Galaga
size = width, height = 224 * 3, 288 * 3
screen = pygame.display.set_mode(size)

ship = ship.Ship(width, height, 3)
timer = pygame.time.Clock()
    
background = generate_starfield(width, height * 10, 1000)
font = load_assets.load_font("PTM55FT.ttf", 16)

offset = -height * 9

while True:

    # Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    keyCheck(ship, keys, mods)

    rend = font.render("FPS: {}".format(timer.get_fps()), 1, (255,255,255))

    screen.fill([0,0,0])
    screen.blit(background, (0, offset))
    screen.blit(rend, (0,0))

    if offset < -height * 3:
        offset += 10

    ship.draw(screen)
    pygame.display.flip()

    timer.tick(60)
