from turtle import Turtle
from constants import SCREEN_HEIGHT, HIGH_SCORE_FILE_PATH
import os


class Board(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.pu()

        self.high_score = 0
        if os.path.exists(HIGH_SCORE_FILE_PATH):
            with open(HIGH_SCORE_FILE_PATH) as high_score_file:
                file_content = high_score_file.read()
                if file_content:
                    self.high_score = int(file_content)

        self.hideturtle()
        self.goto(-70, SCREEN_HEIGHT / 2 - 50)
        self.color("white")
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score: {self.high_score}", False, "left", ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("Arial", 15, "normal"))
        if self.score > self.high_score:
            with open(HIGH_SCORE_FILE_PATH, "w") as high_score_file:
                high_score_file.write(str(self.score))
