from load_assets import load_image
import bullet

class Ship:
    def __init__(self, screenwidth, screenheight, speed):
        self.image = load_image("ship.png")
        self.rect = self.image.get_rect()
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
    
    def shoot(self):
        print("blam!")
