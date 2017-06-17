from Puck import Puck
from Paddle import Paddle
add_library('sound')

def setup():
    size(600, 400)
    global puck
    global left
    global right
    global paddleSpeed
    paddleSpeed = 10
    puck = Puck()
    left = Paddle(True)
    right = Paddle(False)

def draw():
    background(0)

    puck.checkPaddleLeft(left)
    puck.checkPaddleRight(right)

    left.show()
    right.show()
    left.update()
    right.update()

    puck.update()
    puck.edges()
    puck.show()
    
    fill(255)
    textSize(32)
    text(puck.leftscore, 10, 40)
    text(puck.rightscore, width-20, 40)

def keyReleased():
    left.move(0)
    right.move(0)

def keyPressed():
    if key == 'a':
        left.move(-paddleSpeed)
    elif key == 'z':
        left.move(paddleSpeed)

    if key == 'j':
        right.move(-paddleSpeed)
    elif key == 'm':
        right.move(paddleSpeed)