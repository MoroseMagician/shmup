from load_assets import load_image
import pygame
import bullet

class Ship:
    def __init__(self, screenwidth, screenheight, speed):
        self.rect = pygame.rect.Rect(0, 0, 32, 32)
        self.speed = speed

        #Starting position
        self.rect.y = int(0.9 * screenheight)
        self.rect.x = screenwidth // 2 - self.rect.width // 2

        self.hyperbombs = 0
        self.hyperbeams = 0
        self.shotType = "basic"

    def move_left(self, modifier):
        self.rect.x -= self.speed * modifier

    def move_right(self, modifier):
        self.rect.x += self.speed * modifier

    def move_up(self, modifier):
        self.rect.y -= self.speed * modifier

    def move_down(self, modifier):
        self.rect.y += self.speed * modifier
    
    def draw(self, surface):
        pygame.draw.rect(surface, (20, 20, 255), self.rect)

    def shoot(self):
        print("blam!")

    def explode(self):
        None


