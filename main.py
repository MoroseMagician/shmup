import os
import sys
import pygame
import load_assets

pygame.init()
size = 1280, 720
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
    
    if keys[pygame.K_UP]:
        ship_rect = ship_rect.move(0,-speed)
    if keys[pygame.K_DOWN]:
        ship_rect = ship_rect.move(0,speed)
    if keys[pygame.K_LEFT]:
        ship_rect = ship_rect.move(-speed,0)
    if keys[pygame.K_RIGHT]:
        ship_rect = ship_rect.move(speed,0)

    screen.fill([0,0,0])
    screen.blit(ship, ship_rect)
    pygame.display.update()

    timer.tick(60)
