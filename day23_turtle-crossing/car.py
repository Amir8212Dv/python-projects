from turtle import Turtle
from util import generate_random_rgb
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.pu()
        self.setheading(180)
        self.change_color()

        x = random.randint(-SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
        y = self.generate_random_y()
        self.setpos(x, y)

    def change_color(self):
        self.color(generate_random_rgb())

    def reset_position(self):
        self.setpos(SCREEN_WIDTH / 2 + 50, self.generate_random_y())

    def generate_random_y(self):
        return random.randint(-SCREEN_HEIGHT / 2 + 50, SCREEN_HEIGHT / 2 - 80)

    def move(self):
        self.forward(20)
