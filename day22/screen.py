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
        self.set_event_listeners()

    def set_players(self, left_player, right_player):
        self.right_player = right_player
        self.left_player = left_player
        # self.which_player_moves = self.left_player
        self.player_turn = left_player
        self.waiting_player = right_player
        

    def move_up(self):
        self.player_turn.move_up()

    def move_down(self):
        self.player_turn.move_down()

    # def select_right_player(self):
    #     self.which_player_moves = self.right_player

    # def select_left_player(self):
    #     self.which_player_moves = self.left_player

    def switch_player_turn(self):
        self.player_turn, self.waiting_player = self.waiting_player, self.player_turn

    def refresh(self):
        self.screen.update()
        time.sleep(0.1)

    def set_event_listeners(self):
        self.screen.listen()
        self.screen.onkey(fun=self.move_up, key="Up")
        self.screen.onkey(fun=self.move_down, key="Down")
        # self.screen.onkeypress(fun=self.select_right_player, key="Right")
        # self.screen.onkeypress(fun=self.select_left_player, key="Left")
