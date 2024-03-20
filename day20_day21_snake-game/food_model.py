from turtle import Turtle
import random
from data import SCREEN_WIDTH, SCREEN_HEIGHT


class Food:
    def __init__(self):
        food = Turtle("circle")
        food.color("green")
        food.shapesize(0.5)
        food.pu()

        self.food = food
        self.update_food_position()

    def update_food_position(self):
        pos_x = random.randint(-SCREEN_WIDTH / 2 + 30, SCREEN_WIDTH / 2 - 30)
        pos_y = random.randint(-SCREEN_HEIGHT / 2 + 30, SCREEN_HEIGHT / 2 - 30)
        self.food.goto(pos_x, pos_y)
        self.pos = (pos_x, pos_y)

