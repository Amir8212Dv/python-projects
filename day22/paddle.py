from turtle import Turtle
from constants import SCREEN_HEIGHT
from board import Board


class Paddle(Turtle):
    def __init__(self, position: tuple, board: Board):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(4, 0.5, 5)
        self.pu()
        self.goto(position)

        self.board = board
        if self.xcor() < 0:  # It's left paddle
            self.increase_score = self.board.increase_left_score
        else:  # It's right paddle
            self.increase_score = self.board.increase_right_score

    def move_up(self):
        x, y = self.pos()
        if SCREEN_HEIGHT / 2 - 50 > y:
            self.goto(x, y + 40)

    def move_down(self):
        x, y = self.pos()
        if SCREEN_HEIGHT / 2 - 60 > -y:
            self.goto(x, y - 40)
