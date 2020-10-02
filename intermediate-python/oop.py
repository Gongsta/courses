import random

class Blob:
    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)

        
