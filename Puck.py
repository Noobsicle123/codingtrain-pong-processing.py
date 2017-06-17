class Puck(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.r = 12
        self.reset()
        self.rightscore = 0
        self.leftscore = 0

    def checkPaddleLeft(self, p):
        if self.y - self.r < p.y + p.h / 2 and self.y + self.r > p.y - p.h / 2 and self.x - self.r < p.x + p.w / 2:
            if self.x > p.x:
                self.diff = self.y - (p.y - p.h / 2)
                self.rad = radians(45)
                self.angle = map(self.diff, 0, p.h, -self.rad, self.rad)
                self.xspeed = 5 * cos(self.angle)
                self.yspeed = 5 * sin(self.angle)
                self.x = p.x + p.w / 2 + self.r

    def checkPaddleRight(self, p):
        if self.y - self.r < p.y + p.h / 2 and self.y + self.r > p.y - p.h / 2 and self.x + self.r > p.x - p.w / 2:
            if self.x < p.x:
                self.diff = self.y - (p.y - p.h / 2)
                self.rad = radians(135)
                self.angle = map(self.diff, 0, p.h, -self.rad, self.rad)
                self.xspeed = 5 * cos(self.angle)
                self.yspeed = 5 * sin(self.angle)
                self.x = p.x - p.w / 2 - self.r

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def edges(self):
        if self.y < 0 or self.y > height:
            self.yspeed *= -1

        if self.x - self.r > width:
            self.leftscore += 1
            self.reset()

        if self.x + self.r < 0:
            self.rightscore += 1
            self.reset()

    def reset(self):
        self.x = width / 2
        self.y = height / 2
        self.angle = random(-PI / 4, PI / 4)
        self.xspeed = 5 * cos(self.angle)
        self.yspeed = 5 * sin(self.angle)

        if random(1) < 0.5:
            self.xspeed *= -1

    def show(self):
        fill(255)
        ellipse(self.x, self.y, self.r * 2, self.r * 2)