from load_assets import load_image
from shot_types import player

class Bullet(self):
    def __init__(self, screenheight, originX, originY, shotType = "basic"):
        self.image = load_image("{}.png".format(shotType))
        self.speed = 6
        self.damage = 1

