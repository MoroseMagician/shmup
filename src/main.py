import os
import sys
import ship
import pygame
import load_assets

pygame.init()
size = width, height = 224 * 3, 288 * 3
screen = pygame.display.set_mode(size)

ship = ship.Ship(width, height, 3)

timer = pygame.time.Clock()

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
    
while True:
    
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keyCheck(ship, keys, mods)

    screen.fill([0,0,0])
    screen.blit(ship.image, ship.rect)
    pygame.display.update()

    timer.tick(60)
