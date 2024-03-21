from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import random


class Ball(Turtle):
    def __init__(self, left_paddle, right_paddle, refresh_screen, screen_switch_active_paddle):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.pu()
        self.speed("fastest")

        initial_headings = [random.randint(140, 170), random.randint(190, 220)]
        self.setheading(random.choice(initial_headings))

        self.game_is_on = True
        self.active_paddle = left_paddle
        self.inactive_paddle = right_paddle
        self.refresh_screen = refresh_screen
        self.screen_switch_active_paddle = screen_switch_active_paddle
        self.start_moving()

    def switch_active_paddle(self):
        self.active_paddle, self.inactive_paddle = self.inactive_paddle, self.active_paddle
        self.screen_switch_active_paddle()

    def start_moving(self):
        while self.game_is_on:
            # self.forward(20)
            ball_x, ball_y = self.pos()
            paddle_x, paddle_y = self.active_paddle.pos()

            heading = self.heading()
            if abs(paddle_x - ball_x) < 20 and abs(paddle_y - ball_y) < 70:  # If ball hits the active paddle
                self.setheading(180 - heading + random.randint(-5, 5))
                self.switch_active_paddle()
            elif SCREEN_HEIGHT / 2 - ball_y < 30:  # If ball hits the Upper Wall
                extra_curvature = 0
                if heading < 20:  # Left to Right reflection
                    extra_curvature = -(random.randint(10, 20))
                elif heading < 40:  # Left to Right reflection
                    extra_curvature = -(random.randint(0, 5))
                elif heading > 160:  # Right to Left reflection
                    extra_curvature = random.randint(10, 20)
                elif heading < 140:  # Right to left reflection
                    extra_curvature = random.randint(0, 5)

                self.setheading(360 - heading + extra_curvature)
            elif SCREEN_HEIGHT / 2 + ball_y < 30:  # If ball hits the Lower Wall
                # If the reflection angle is too obtuse, make it less obtuse
                extra_curvature = 0
                if heading < 200:  # Right to Left reflection
                    extra_curvature = -(random.randint(10, 20))
                elif heading < 220:  # Right to Left reflection
                    extra_curvature = -(random.randint(0, 5))
                elif heading > 340:  # Left to Right reflection
                    extra_curvature = random.randint(10, 20)
                elif heading < 320:  # Left to Right reflection
                    extra_curvature = random.randint(0, 5)

                self.setheading(360 - heading + extra_curvature)
            elif SCREEN_WIDTH / 2 - abs(ball_x) < 20:  # If ball hits the vertical wall
                print("YOU LOSE")
                break

            self.forward(20)
            self.refresh_screen()
