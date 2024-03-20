from food import Food
from screen import GameScreen
from board import Board
from snake import Snake
from util import calculate_two_points_distance

screen = GameScreen()
snake = Snake(screen.easyMode)
board = Board()
food = Food()


is_snake_alive = True
while is_snake_alive:

    is_snake_alive = snake.move(screen.move_steps)

    if calculate_two_points_distance(snake.head_pos, food.pos()) < 15:
        board.increase_score()
        food.update_position()
        snake.generate_new_segment()

    screen.refresh()

board.game_over()
screen.screen.exitonclick()
