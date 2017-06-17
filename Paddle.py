class Paddle(object):

    def __init__(self, left):
        self.y = height / 2
        self.w = 20
        self.h = 100

        self.ychange = 0

        if left:
            self.x = self.w
        else:
            self.x = width - self.w

    def update(self):
        self.y += self.ychange
        self.y = self.y = constrain(self.y, self.h / 2, height - self.h / 2)

    def move(self, steps):
        self.ychange = steps

    def show(self):
        fill(255)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)