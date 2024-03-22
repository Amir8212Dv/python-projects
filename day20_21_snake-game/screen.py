from turtle import Screen
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MOVE_STEP_SIZE
import time


class GameScreen:
    def __init__(self, game_over_fn):
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.title("Snake Game")
        screen.tracer(0)
        self.easyMode = screen.textinput(title="Game Mode" ,prompt="easy or hard? ").lower() == "easy"

        self.move_steps = (MOVE_STEP_SIZE, 0)
        self.screen = screen
        self.game_over_fn = game_over_fn
        self.is_game_on = True
        self.set_event_listeners()

    def turn_up(self):
        if self.move_steps[1] == 0:  # If it's heading down, don't turn up
            self.move_steps = (0, MOVE_STEP_SIZE)

    def turn_down(self):
        if self.move_steps[1] == 0:  # If it's heading up, don't turn down
            self.move_steps = (0, -MOVE_STEP_SIZE)

    def turn_right(self):
        if self.move_steps[0] == 0:  # If it's heading left, don't turn right
            self.move_steps = (MOVE_STEP_SIZE, 0)

    def turn_left(self):
        if self.move_steps[0] == 0:  # If it's heading right, don't turn left
            self.move_steps = (-MOVE_STEP_SIZE, 0)

    def refresh(self):
        self.screen.update()
        time.sleep(0.1)

    def game_over(self):
        self.screen.update()
        time.sleep(3)
        self.move_steps = (MOVE_STEP_SIZE, 0)

    def exit_game(self):
        self.game_over_fn()
        self.is_game_on = False
        self.screen.bye()

    def set_event_listeners(self):
        self.screen.listen()
        self.screen.onkey(fun=self.turn_up, key="Up")
        self.screen.onkey(fun=self.turn_down, key="Down")
        self.screen.onkey(fun=self.turn_right, key="Right")
        self.screen.onkey(fun=self.turn_left, key="Left")
        self.screen.onkey(fun=self.exit_game, key="Escape")
