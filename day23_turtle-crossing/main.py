from car import Car
from crossing_turtle import CrossingTurtle
from screen import GameScreen
from constants import SCREEN_WIDTH
from board import Board

board = Board()
screen = GameScreen()


def level_up():
    global board, screen
    board.level_up()
    screen.increase_game_speed()


turtle = CrossingTurtle(level_up)
screen.set_event_listeners(turtle.move_up, turtle.move_down)

cars = []
for i in range(15):
    car = Car()
    cars.append(car)

is_game_on = True
while is_game_on:
    for car in cars:
        car.move()
        if turtle.distance(car) < 20:
            print("YOU LOSE")
            is_game_on = False

        if car.xcor() < -SCREEN_WIDTH / 2:
            car.reset_position()
            car.change_color()

    screen.refresh()

screen.screen.exitonclick()
