class Square(object):
    def __init__(self, image, size, x, y):
        self.revealed = False
        self.flagged = False
        self.mine_count = 0
        self.is_mined = False
        self.mine_pressed = False
        self.square_size = size
        self.x = x
        self.y = y
        self.image = image

    def checkcollision(self, a, b):
        if self.x <= a < self.x + self.square_size and self.y <= b < self.y+self.square_size:
            return True
        else:
            return False
