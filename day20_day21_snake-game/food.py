from turtle import Turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5)
        self.pu()

        self.update_position()

    def update_position(self):
        pos_x = random.randint(-SCREEN_WIDTH / 2 + 30, SCREEN_WIDTH / 2 - 30)
        pos_y = random.randint(-SCREEN_HEIGHT / 2 + 30, SCREEN_HEIGHT / 2 - 30)
        self.goto(pos_x, pos_y)
        self.pos = (pos_x, pos_y)
