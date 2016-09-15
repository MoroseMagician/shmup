import os
import sys
import pygame
import load_assets

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

ship = load_assets.load_image("ship.png")
ship_rect = ship.get_rect()

timer = pygame.time.Clock()

while True:
    
    speed = 4
    keys = pygame.key.get_pressed()
    modifiers = pygame.key.get_mods()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if modifiers & pygame.KMOD_LSHIFT:
        speed = 2
    
    if keys[pygame.K_UP] and ship_rect[1] > 0:
        ship_rect = ship_rect.move(0,-speed)
    if keys[pygame.K_DOWN] and ship_rect[1] + ship_rect[2] < height:
        ship_rect = ship_rect.move(0,speed)
    if keys[pygame.K_LEFT] and ship_rect[0] > 0:
        ship_rect = ship_rect.move(-speed,0)
    if keys[pygame.K_RIGHT] and ship_rect[0] + ship_rect[3] < width:
        ship_rect = ship_rect.move(speed,0)

    screen.fill([0,0,0])
    screen.blit(ship, ship_rect)
    pygame.display.update()

    timer.tick(60)
