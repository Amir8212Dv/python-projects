from turtle import Turtle
import random
from paddle import Paddle


class Ball(Turtle):
    def __init__(self, left_paddle: Paddle, right_paddle: Paddle):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.pu()

        # Game always starts with the left paddle
        initial_headings = [random.randint(140, 170), random.randint(190, 220)]
        self.setheading(random.choice(initial_headings))

        self.active_paddle = left_paddle
        self.inactive_paddle = right_paddle

    def switch_active_paddle(self):
        self.active_paddle, self.inactive_paddle = self.inactive_paddle, self.active_paddle

    def hit_upper_wall(self):
        heading = self.heading()
        # If the reflection angle is too obtuse, make it less obtuse
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
        self.move()  # To prevent ball from reverting bug

    def hit_lower_wall(self):
        heading = self.heading()
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
        self.move()  # To prevent ball from reverting bug

    def hit_active_paddle(self):
        self.setheading(180 - self.heading() + random.randint(-5, 5))
        self.switch_active_paddle()

    def hit_side_walls(self):
        self.goto(0, 0)
        self.setheading(self.heading() + 180)
        self.inactive_paddle.increase_score()
        self.switch_active_paddle()

    def move(self):
        self.forward(20)
