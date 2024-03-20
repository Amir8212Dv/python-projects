from turtle import Turtle
from constants import SCREEN_HEIGHT


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(-30, SCREEN_HEIGHT / 2 - 50)
        self.color("white")
        self.update_board()

    def gain(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score : {self.score}", False, "left", ("Arial", 15, "normal"))
