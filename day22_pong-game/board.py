from turtle import Turtle
from constants import SCREEN_HEIGHT


class Board(Turtle):
    def __init__(self):
        super().__init__()

        self.left_score = 0
        self.right_score = 0
        self.pu()
        self.hideturtle()
        self.color("white")
        self.goto(0, SCREEN_HEIGHT / 2 - 70)
        self.update_scores()

        line_turtle = Turtle()
        line_turtle.pu()
        line_turtle.hideturtle()
        line_turtle.color("white")
        line_turtle.goto(0, -SCREEN_HEIGHT / 2)
        line_turtle.write("|\n" * 100, False, "center", ("Courier", 10, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_scores()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"{self.left_score}      {self.right_score}", False, "center", ("Courier", 50, "normal"))
