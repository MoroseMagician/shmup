import os
import sys
import ship
import enemy
import bullet
import pygame
import load_assets
from random import randint

spawncooldown = 500
last_spawn = pygame.time.get_ticks()

def keyCheck(ship, speed = 2):
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    
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

    if keys[pygame.K_a]:
        shoot(ship, shift)

    if keys[pygame.K_s]:
        global beamactive 
        beamactive = True
        uitext["Beam"] = font.render("Beam: ACTIVE", 1, (255,255,255))
        shoot_hyperbeam()
    else:
        global beamactive 
        beamactive = False
        uitext["Beam"] = font.render("Beam: INACTIVE", 1, (255,0,255))
        
    if keys[pygame.K_ESCAPE]:
        sys.exit()

def shoot(ship, shift):
    current = pygame.time.get_ticks()

    if current - ship.cooldown >= ship.shotdelay:
        bullets.add(bullet.Bullet(height, ship.rect.x + ship.rect.width // 2, ship.rect.y))
        ship.cooldown = current

def shoot_hyperbeam():
    None

def spawn_enemies():
    for i in range(3, 0, -1):
        for n in range(100, width - 100, 50):
            enemies.add(enemy.SmallEnemy((n, -i * 50), (0, 1), 0, 300 - 50 * i))

def spawn_stragglers(last_spawn):
    current = pygame.time.get_ticks()
    if current - last_spawn >= spawncooldown:
        enemies.add(enemy.DumbEnemy(1, randint(20, width - 20), height + 10))
        return current
    return last_spawn

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
enemies = pygame.sprite.Group()

hyperbeam = bullet.HyperBeam(height)
beamactive = False

uitext = {}

#spawn_enemies()

# Stuff that's only used in the menu loop
menu_logo = pygame.sprite.Sprite()
menu_logo.image = load_assets.load_image("logo.png").convert()
menu_font = load_assets.load_font("PTM55FT.ttf", 32)
cursor = pygame.Surface((20, 20))
cursor_position = 0
menu_element_positions = [500, 550, 600]

menu_loop = True
while menu_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                cursor_position = (cursor_position + 1) % 3
            elif event.key == pygame.K_UP:
                cursor_position -= 1
                if cursor_position == -1:
                    cursor_position = 2
            elif event.key == pygame.K_RETURN:
                if cursor_position == 0:
                    menu_loop = False
                elif cursor_position == 1:
                    sys.exit()
                else:
                    #TODO: Add options?
                    pass

    screen.fill([0,0,0])

    text = []
    text.append(menu_font.render("START", 1, (255, 255, 255)))
    text.append(menu_font.render("QUIT", 1, (255, 255, 255)))
    text.append(menu_font.render("OPTIONS", 1, (255, 255, 255)))

    for i, t in enumerate(text):
        screen.blit(t, (width // 2 - 50, menu_element_positions[i]))
    pygame.draw.polygon(cursor, (255, 0, 0), [(0, 0), (0, 20), (20, 10)])

    #Cursor position debug
    # tbla = menu_font.render("pos: {}".format(cursor_position), 1, (255, 255, 255))
    # screen.blit(tbla, (0, height - 100))

    screen.blit(cursor, (width // 2 - 100, menu_element_positions[cursor_position] + 4))
    screen.blit(menu_logo.image, (10, 100))
    pygame.display.set_caption("Main Menu")
    

    pygame.display.flip()
    timer.tick(60)

while True:
    # This is the main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keyCheck(ship)
    pygame.display.set_caption("Untitled SHMUP!")

    last_spawn = spawn_stragglers(last_spawn)

    uitext["FPS"] =  font.render("FPS: {}".format(timer.get_fps()), 1, (255,255,255))
    uitext["Bullets"] = font.render("Bullets: {}".format(len(bullets.sprites())), 1, (255,255,255))
    uitext["Enemies"] = font.render("Enemies: {}".format(len(enemies.sprites())), 1, (255,255,255))
    uitext["Respawns"] = font.render("Ship lives: {}".format(ship.respawns), 1, (255,255,255))

    screen.fill([0,0,0])
    screen.blit(background, (0, offset))
    screen.blit(ship.image, ship.rect)

    bullets.update()
    bullets.draw(screen)

    enemies.update()
    enemies.draw(screen)

    hyperbeam.update(ship.rect.x + 8, ship.rect.y - height, beamactive)

    if beamactive:
        screen.blit(hyperbeam.image, hyperbeam.rect)

    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    beamhits = pygame.sprite.spritecollide(hyperbeam, enemies, True, False)
    collision = pygame.sprite.spritecollide(ship, enemies, True)

    spawncooldown -= len(beamhits)

    if len(collision) == 1:
        ship.explode()

    #TODO: Make a smooth background transition
    #      Try to append a second background to the current one somehow
    #      Find a way to do this without wasting resources
    if offset < -height * 2:
        offset += 20
    else:
        offset = -height * 9

    for i, t in enumerate(uitext):
        screen.blit(uitext[t], (0, i * 20))

    pygame.display.flip()

    timer.tick(60)
