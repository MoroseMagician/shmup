import pygame
from load_assets import load_image
from shot_types import player

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screenheight, originX, originY, shotType = "basic"):
        
        pygame.sprite.Sprite.__init__(self)

        #self.image = load_image("{}.png".format(shotType)).convert()
        self.image = pygame.Surface([5, 7]).convert()
        self.image.fill([255,255,0])

        self.rect = self.image.get_rect()
        self.rect.x = originX
        self.rect.y = originY

        self.speed = 8
        self.damage = player[shotType]

    
    def update(self):
        if self.rect.y <= 0:
            self.kill()
        else:
            self.rect.y -= self.speed
