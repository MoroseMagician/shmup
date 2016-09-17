import os
import sys
import ship
import bullet
import pygame
import load_assets
from random import randint

def keyCheck(ship, keys, mods, speed = 2):
    
    shift = False

    if mods & pygame.KMOD_LSHIFT:
        speed = 1
        shift = True

    if keys[pygame.K_UP] and ship.rect.y > 0:
        ship.move_up(speed)
    if keys[pygame.K_DOWN] and ship.rect.y + ship.rect.height < height:
        ship.move_down(speed)
    if keys[pygame.K_LEFT] and ship.rect.x > 0:
        ship.move_left(speed)
    if keys[pygame.K_RIGHT] and ship.rect.x + ship.rect.width < width:
        ship.move_right(speed)

    if keys[pygame.K_z]:
        current = pygame.time.get_ticks()
        if current - ship.cooldown >= ship.shotdelay:
            if shift:
                bullets.add(bullet.Bullet(height, ship.rect.x + ship.rect.width // 2 - 5, ship.rect.y))
                bullets.add(bullet.Bullet(height, ship.rect.x + ship.rect.width // 2 + 5, ship.rect.y))
            else:
                bullets.add(bullet.Bullet(height, ship.rect.x + ship.rect.width, ship.rect.y))
                bullets.add(bullet.Bullet(height, ship.rect.x, ship.rect.y))

            ship.cooldown = current

    if keys[pygame.K_ESCAPE]:
        sys.exit()

pygame.init()

# 224x288 is the original arcade resolution for Galaga
size = width, height = 224 * 3, 288 * 3
screen = pygame.display.set_mode(size)

ship = ship.Ship(width, height, 3)
timer = pygame.time.Clock()
    
background = load_assets.generate_starfield(width, height * 10, 200)
font = load_assets.load_font("PTM55FT.ttf", 16)

offset = -height * 9

bullets = pygame.sprite.Group()
stars = pygame.sprite.Group()

while True:

    # Main game loop
    #TODO: Clean up this fucking mess
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    keyCheck(ship, keys, mods)

    rend = font.render("FPS: {}".format(timer.get_fps()), 1, (255,0,255))
    boolets = font.render("boolets: {}".format(len(bullets.sprites())), 1, (255,0,255))

    screen.fill([0,0,0])
    screen.blit(background, (0, offset))
    screen.blit(ship.image, ship.rect)

    bullets.update()
    bullets.draw(screen)

    screen.blit(rend, (0,0))
    screen.blit(boolets, (0, 30))

    #TODO: Make a smooth background transition
    #      Try to append a second background to the current one somehow
    #      Find a way to do this without wasting resources
    if offset < -height * 2:
        offset += 10
    else:
        offset = -height * 9

    pygame.display.flip()

    timer.tick(60)
