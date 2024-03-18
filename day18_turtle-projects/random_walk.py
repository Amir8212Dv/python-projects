from turtle import Turtle, Screen, colormode
import random
from util import generate_random_rgb

the_turtle = Turtle("arrow")
screen = Screen()
colormode(255)

the_turtle.speed("fastest")
the_turtle.pensize(15)

angles = [0, 90, 180, 270]


while True:
    max_x, max_y = screen.screensize()
    pos_x, pos_y = the_turtle.position()
    if abs(pos_x) > max_x + 40 or abs(pos_y) > max_y + 40:
        break

    the_turtle.pencolor(generate_random_rgb())
    the_turtle.right(random.choice(angles))
    the_turtle.forward(40)

screen.exitonclick()
