from turtle import Turtle
from constants import SCREEN_HEIGHT,SCREEN_WIDTH

class Player(Turtle):
    def __init__(self, side: str):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(4,0.5,5)
        self.pu()
        if side == "left":
            self.goto(-SCREEN_WIDTH / 2 + 20, 0)
        elif side == "right":
            self.goto(SCREEN_WIDTH / 2 - 20, 0)

    def move_up(self):
        x,y = self.pos()
        if SCREEN_HEIGHT / 2 - 50 > y:
            self.goto(x, y + 20)

    def move_down(self):
        x,y = self.pos()
        if SCREEN_HEIGHT / 2 - 60 > -y:
            self.goto(x, y - 20)