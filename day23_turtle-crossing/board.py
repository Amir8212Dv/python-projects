from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Board(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-SCREEN_WIDTH / 2 + 70, SCREEN_HEIGHT / 2 - 70)
        self.update_board()

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 20, "normal"))

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", ("Courier", 20, "normal"))
