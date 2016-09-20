from load_assets import load_image
import pygame
import bullet

class Ship:
    def __init__(self, screenwidth, screenheight, speed):

        self.image = pygame.Surface([32, 32]).convert()
        self.image.fill([255,255,255])
        self.rect = pygame.rect.Rect(0, 0, 32, 32)
        self.speed = speed

        #Starting position
        self.startX = int(0.9 * screenheight)
        self.startY = screenwidth // 2 - self.rect.width // 2
        self.rect.y = self.startX
        self.rect.x = self.startY

        self.hyperbombs = 0
        self.hyperbeams = 0
        self.shotType = "basic"
        self.respawns = 3

        # 0.5 second shot cooldown
        self.shotdelay = 0
        self.cooldown = pygame.time.get_ticks()

    def move_left(self, modifier):
        self.rect.x -= self.speed * modifier

    def move_right(self, modifier):
        self.rect.x += self.speed * modifier

    def move_up(self, modifier):
        self.rect.y -= self.speed * modifier

    def move_down(self, modifier):
        self.rect.y += self.speed * modifier

    def explode(self):
        self.rect.y = self.startX
        self.rect.x = self.startY


        self.respawns -= 1


