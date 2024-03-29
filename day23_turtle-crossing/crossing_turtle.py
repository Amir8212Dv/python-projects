from turtle import Turtle
from constants import SCREEN_HEIGHT


class CrossingTurtle(Turtle):
    def __init__(self, level_up_fn):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.initial_y = -SCREEN_HEIGHT / 2 + 20
        self.setpos(0, self.initial_y)
        self.level_up_fn = level_up_fn
        self.move_distance = 10
        self.game_is_one = True

    def move_up(self):
        if not self.game_is_one:
            return

        if self.ycor() < SCREEN_HEIGHT / 2 - 30:
            self.forward(10)
        else:
            self.level_up()

    def level_up(self):
        if not self.game_is_one:
            return
        self.goto(0, self.initial_y)
        self.level_up_fn()
        self.move_distance *= 1.1  # Increase by 10 percent

    def move_down(self):
        if not self.game_is_one:
            return
        if self.ycor() > self.initial_y:
            self.backward(10)

    def game_over(self):
        self.game_is_one = False
