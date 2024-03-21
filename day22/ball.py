from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import random


class Ball(Turtle):
    def __init__(self, left_player, right_player, refresh_screen, screen_switch_player):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.pu()
        self.speed("fastest")

        initial_headings = [random.randint(140, 170), random.randint(190, 220)]
        self.setheading(random.choice(initial_headings))

        self.game_is_on = True
        self.player_turn = left_player
        self.waiting_player = right_player
        self.refresh_screen = refresh_screen
        self.screen_switch_player = screen_switch_player
        self.start_moving()

    def switch_player_turn(self):
        self.player_turn, self.waiting_player = self.waiting_player, self.player_turn
        self.screen_switch_player()

    def start_moving(self):
        while self.game_is_on:
            self.forward(20)
            ball_x, ball_y = self.pos()
            player_x, player_y = self.player_turn.pos()

            heading = self.heading()
            if abs(player_x - ball_x) < 20 and abs(player_y - ball_y) < 70:
                self.setheading(180 - heading + random.randint(-5, 5))
                self.forward(50)
                self.switch_player_turn()
            elif SCREEN_HEIGHT / 2 - ball_y < 30:  # If ball hits the Upper Wall
                extra_curvature = 0
                if heading < 20:
                    extra_curvature = -(random.randint(10, 20))
                elif heading < 40:
                    extra_curvature = -(random.randint(0, 5))
                elif heading > 160:
                    extra_curvature = random.randint(10, 20)
                elif heading < 140:
                    extra_curvature = random.randint(0, 5)

                self.setheading(360 - heading + extra_curvature)
                self.forward(20)
            elif SCREEN_HEIGHT / 2 + ball_y < 30:  # If ball hits the Lower Wall
                extra_curvature = 0
                if heading < 200:
                    extra_curvature = -(random.randint(10, 20))
                elif heading < 220:
                    extra_curvature = -(random.randint(0, 5))
                elif heading > 340:
                    extra_curvature = random.randint(10, 20)
                elif heading < 320:
                    extra_curvature = random.randint(0, 5)

                self.setheading(360 - heading + extra_curvature)
                self.forward(20)
            elif SCREEN_WIDTH / 2 - abs(ball_x) < 20:
                print("YOU LOSE")
                break
            self.refresh_screen()
