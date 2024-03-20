from food_model import Food
from screen_model import GameScreen
from score_model import Score
from snake_model import Snake
from util import calculate_snake_distance_from_point

screen = GameScreen()
snake = Snake()
score = Score()
food = Food()


is_snake_alive = True
while is_snake_alive:
    screen.update()

    is_snake_alive = snake.update_head_position(screen.x_change, screen.y_change)

    if calculate_snake_distance_from_point(snake.head_pos, food.pos) < 15:
        score.gain_score()
        food.update_food_position()
        snake.generate_new_segment()

    for i in range(len(snake.segments)):
        snake.segments[i].goto(snake.segments_pos[i])


screen.screen.exitonclick()
