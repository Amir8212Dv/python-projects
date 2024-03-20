from turtle import Turtle
from constants import SCREEN_HEIGHT


class Score:
    def __init__(self):
        score_turtle = Turtle()
        score_turtle.hideturtle()
        score_turtle.pu()
        score_turtle.goto(-30, SCREEN_HEIGHT / 2 - 50)
        score_turtle.color("white")
        self.score_turtle = score_turtle
        self.score = 0
        self.update_board()

    def gain(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Score : {self.score}", False, "left", ("Arial", 15, "normal"))
