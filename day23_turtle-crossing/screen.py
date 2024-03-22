from turtle import Screen
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import time


class GameScreen:
    def __init__(self):
        screen = Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.title("Turtle Crossing Game")
        screen.tracer(0)
        screen.colormode(255)

        self.screen = screen
        self.game_speed = 0.1

    def refresh(self):
        self.screen.update()
        time.sleep(self.game_speed)

    def increase_game_speed(self):
        """Increases the game speed by 10%"""
        self.game_speed *= 0.9

    def set_event_listeners(self, move_up_fn, move_down_fn):
        self.screen.listen()
        self.screen.onkey(fun=move_up_fn, key="Up")
        self.screen.onkey(fun=move_down_fn, key="Down")
