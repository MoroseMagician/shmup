import pygame
import load_assets

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, origin, movement, speed, stop):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([32, 32]).convert()
        self.image.fill([255,0,0])
        self.rect = self.image.get_rect()

        self.x, self.y = origin
        self.moveX, self.moveY = movement
        self.stop = stop

        self.rect.x = self.x
        self.rect.y = self.y
        self.spawning = True

        self.speed = speed
        self.stepping = 0

    def update(self, width, horizontalstep = 0):
        if self.spawning:
            if self.rect.y > self.stop:
                self.spawning = False
            else:
                self.rect.y += self.moveY
                self.rect.x += self.moveX
        elif horizontalstep != 0:
            if self.rect.x > width or self.rect.x < 0:
                self.rect.y += 10
                self.stepping = -self.stepping
            else:
                self.rect.x += self.stepping

class LargeEnemy(pygame.sprite.Sprite):
    def __init__(self):
        None

class HugeEnemy(pygame.sprite.Sprite):
    def __init__(self):
        None

class DumbEnemy(pygame.sprite.Sprite):
    def __init__(self, speed, x, killheight):
       
        pygame.sprite.Sprite.__init__(self)

        #self.image = pygame.Surface([16, 16]).convert()
        self.image = load_assets.load_image("enemy.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = -20
        self.speed = speed
        self.killheight = killheight

    def update(self):
        if self.rect.y >= self.killheight:
            self.kill()
        else:
            self.rect.y += self.speed



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        None

