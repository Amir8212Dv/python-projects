from screen import GameScreen
from paddle import Paddle
from ball import Ball
from constants import SCREEN_WIDTH
from board import Board
from constants import SCREEN_HEIGHT

screen = GameScreen()

board = Board()
left_paddle = Paddle((-SCREEN_WIDTH / 2 + 20, 0), board)
right_paddle = Paddle((SCREEN_WIDTH / 2 - 20, 0), board)
screen.set_paddles(left_paddle, right_paddle)
ball = Ball(left_paddle, right_paddle)

while True:
    ball_x, ball_y = ball.pos()
    paddle_x, paddle_y = ball.active_paddle.pos()

    if abs(paddle_x - ball_x) < 20 and abs(paddle_y - ball_y) < 70:
        ball.hit_active_paddle()
        screen.increase_game_speed()
        screen.switch_active_paddle()
    elif SCREEN_WIDTH / 2 - abs(ball_x) < 20:
        ball.hit_side_walls()
        screen.switch_active_paddle()
    elif SCREEN_HEIGHT / 2 - ball_y < 20:
        ball.hit_upper_wall()
    elif SCREEN_HEIGHT / 2 + ball_y < 20:
        ball.hit_lower_wall()

    ball.move()
    screen.refresh()
