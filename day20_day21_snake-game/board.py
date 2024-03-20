from turtle import Turtle
from constants import SCREEN_HEIGHT


class Board(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(-30, SCREEN_HEIGHT / 2 - 50)
        self.color("white")
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}", False, "left", ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("Arial", 15, "normal"))
