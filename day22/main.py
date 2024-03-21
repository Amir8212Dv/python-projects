from screen import GameScreen
from paddle import Paddle
from ball import Ball

screen = GameScreen()
left_paddle = Paddle("left")
right_paddle = Paddle("right")

screen.set_paddles(left_paddle, right_paddle)
ball = Ball(left_paddle, right_paddle, screen.refresh, screen.switch_active_paddle)
screen.refresh()

screen.screen.exitonclick()
