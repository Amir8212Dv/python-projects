from food import Food
from screen import GameScreen
from score import Score
from snake import Snake
from util import calculate_snake_distance_from_point

screen = GameScreen()
snake = Snake(screen.easyMode)
score = Score()
food = Food()


is_snake_alive = True
while is_snake_alive:

    is_snake_alive = snake.move(screen.move_steps)

    if calculate_snake_distance_from_point(snake.head_pos, food.pos) < 15:
        score.gain()
        food.update_position()
        snake.generate_new_segment()

    screen.refresh()


screen.screen.exitonclick()
