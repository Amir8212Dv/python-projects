from screen import GameScreen
from paddle import Paddle
from ball import Ball
from constants import SCREEN_WIDTH

screen = GameScreen()
left_paddle = Paddle((-SCREEN_WIDTH / 2 + 20, 0))
right_paddle = Paddle((SCREEN_WIDTH / 2 - 20, 0))

screen.set_paddles(left_paddle, right_paddle)
ball = Ball(left_paddle, right_paddle, screen.refresh, screen.switch_active_paddle)
screen.refresh()

screen.screen.exitonclick()
