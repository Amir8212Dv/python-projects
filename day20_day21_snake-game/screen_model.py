from turtle import Screen
from data import SCREEN_HEIGHT, SCREEN_WIDTH, MOVE_STEPS
import time


class GameScreen:
    def __init__(self):
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.title("Snake Game")
        screen.tracer(0)

        self.x_change = MOVE_STEPS
        self.y_change = 0
        self.screen = screen
        self.set_event_listeners()

    def turn_up(self):
        self.x_change = 0
        self.y_change = MOVE_STEPS

    def turn_down(self):
        self.x_change = 0
        self.y_change = -MOVE_STEPS

    def turn_right(self):
        self.x_change = MOVE_STEPS
        self.y_change = 0

    def turn_left(self):
        self.x_change = -MOVE_STEPS
        self.y_change = 0

    def update(self):
        self.screen.update()
        time.sleep(0.1)

    def set_event_listeners(self):
        self.screen.onkey(fun=self.turn_up, key="Up")
        self.screen.onkey(fun=self.turn_down, key="Down")
        self.screen.onkey(fun=self.turn_right, key="Right")
        self.screen.onkey(fun=self.turn_left, key="Left")
