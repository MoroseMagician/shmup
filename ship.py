class Ship:
    def __init__(self, image, image_rect, height, speed):
        self.speed = speed
        self.image = image
        self.position = image_rect.move(0, height)
