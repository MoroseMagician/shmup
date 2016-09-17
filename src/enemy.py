import pygame

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, origin, movement, speed, stop):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([16, 16]).convert()
        self.image.fill([255,0,0])
        self.rect = self.image.get_rect()

        self.x, self.y = origin
        self.moveX, self.moveY = movement
        self.stop = stop

        self.rect.x = self.x
        self.rect.y = self.y
        self.spawning = True

        self.speed = speed

    def update(self):
        if self.spawning:
            if self.rect.y > self.stop:
                self.spawning = False
            else:
                self.rect.y += self.moveY
                self.rect.x += self.moveX
        else:
            #TODO: Don't use magic numbers!
            if self.rect.x > (224 * 3) or self.rect.x < 0:
                self.speed = -self.speed
            self.rect.x += self.speed

class LargeEnemy(pygame.sprite.Sprite):
    def __init__(self):
        None

class HugeEnemy(pygame.sprite.Sprite):
    def __init__(self):
        None

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        None

