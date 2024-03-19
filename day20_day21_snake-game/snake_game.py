from turtle import Turtle, Screen, shape
import time
import random


screen = Screen()
screen.bgcolor("black")
screen_width = 900
screen_height = 800
screen.setup(width=screen_width, height=screen_height)
screen.title("Snake Game")

score = 0

text_turtle = Turtle()
text_turtle.hideturtle()
text_turtle.pu()
text_turtle.goto(-30, screen_height / 2 - 50)
text_turtle.color("white")


def update_score(score: int):
    text_turtle.clear()
    text_turtle.write(f"Score : {score}", False, "left", ("Arial", 15, "normal"))


screen.tracer(0)

move_steps = 20

segments_pos = []
segments = []  # [seg3 , seg2 , head]


def generate_new_segment(pos: tuple = None, backward: int = 0):
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    if pos:
        segment.goto(pos)
    elif backward:
        segment.backward(backward)

    global segments, segments_pos
    segments.insert(0, segment)
    segments_pos.insert(0, segment.pos())


for i in range(3):
    generate_new_segment(backward=i * 20)

screen.update()

x_change, y_change = move_steps, 0


def turn_up():
    global x_change, y_change
    x_change = 0
    y_change = move_steps


def turn_down():
    global x_change, y_change
    x_change = 0
    y_change = -move_steps


def turn_right():
    global x_change, y_change
    x_change = move_steps
    y_change = 0


def turn_left():
    global x_change, y_change
    x_change = -move_steps
    y_change = 0


screen.onkey(fun=turn_up, key="Up")
screen.onkey(fun=turn_down, key="Down")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=turn_left, key="Left")


food_turtle = Turtle("circle")
food_turtle.color("green")
food_turtle.shapesize(0.5)
food_turtle.pu()
food_x, food_y = food_turtle.pos()


def update_food_position():
    global food_x, food_y, food_turtle

    food_x = random.randint(-screen_width / 2 + 30, screen_width / 2 - 30)
    food_y = random.randint(-screen_height / 2 + 30, screen_height / 2 - 30)
    food_turtle.goto(food_x, food_y)
    screen.update()


update_food_position()

is_snake_alive = True
while is_snake_alive:
    update_score(score)
    screen.update()
    time.sleep(0.1)

    head_x, head_y = segments_pos[-1]
    head_x += x_change
    head_y += y_change
    segments_pos.append((head_x, head_y))

    snake_tale = segments_pos[0]
    segments_pos.remove(snake_tale)

    if (
        abs(food_x - head_x) < 15 and abs(food_y - head_y) < 15
    ):  # Check if snakes head's distance with food is less than 15 then consider it as ate
        score += 1
        update_score(score)
        update_food_position()
        generate_new_segment(snake_tale)

    for i in range(len(segments_pos) - 1):
        x, y = segments_pos[i]
        if x == head_x and y == head_y:
            is_snake_alive = False
            break

    for i in range(len(segments)):
        segments[i].goto(segments_pos[i])
        if abs(head_x) + 20 >= screen_width / 2 or abs(head_y) + 20 >= screen_height / 2:
            print("Snake died")
            is_snake_alive = False
            break

screen.exitonclick()
