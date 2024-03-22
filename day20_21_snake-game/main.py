from food import Food
from screen import GameScreen
from board import Board
from snake import Snake
from util import calculate_two_points_distance
import time

board = Board()
screen = GameScreen(board.game_over)
snake = Snake(screen.easyMode)
food = Food()


while screen.is_game_on:

    is_snake_alive = snake.move(screen.move_steps)

    if calculate_two_points_distance(snake.head_pos, food.pos()) < 15:
        board.increase_score()
        food.update_position()
        snake.generate_new_segment()

    if not is_snake_alive:
        board.game_over()
        snake.game_over()
        screen.refresh()
        time.sleep(3)
        snake = Snake(snake.easyMode)
        board.reset()

    screen.refresh()

screen.screen.exitonclick()
