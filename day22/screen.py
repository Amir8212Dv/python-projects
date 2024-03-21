from turtle import Screen
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import time


class GameScreen:
    def __init__(self):
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.title("Pong")
        screen.tracer(0)

        self.screen = screen
        self.game_speed = 0.1
        self.set_event_listeners()

    def set_paddles(self, left_paddle, right_paddle):
        self.active_paddle = left_paddle
        self.inactive_paddle = right_paddle

    def move_up(self):
        self.active_paddle.move_up()

    def move_down(self):
        self.active_paddle.move_down()

    def switch_active_paddle(self):
        self.active_paddle, self.inactive_paddle = self.inactive_paddle, self.active_paddle

    def refresh(self):
        self.screen.update()
        time.sleep(self.game_speed)

    def increase_game_speed(self):
        """Increases the game speed by 1%"""
        self.game_speed -= self.game_speed / 100 

    def set_event_listeners(self):
        self.screen.listen()
        self.screen.onkey(fun=self.move_up, key="Up")
        self.screen.onkey(fun=self.move_down, key="Down")
