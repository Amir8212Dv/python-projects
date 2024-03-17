from turtle import Turtle, Screen
import random


the_turtle = Turtle("arrow")
the_turtle.speed("fastest")
the_turtle.pensize(15)

screen = Screen()

colors = [
    "blue",
    "green",
    "red",
    "yellow",
    "orange",
    "brown",
    "black",
]
angles = [0, 90, 180, 270]


while True:
    max_x, max_y = screen.screensize()
    pos_x, pos_y = the_turtle.position()
    if abs(pos_x) > max_x + 40 or abs(pos_y) > max_y + 40:
        break

    the_turtle.color(random.choice(colors))
    the_turtle.right(random.choice(angles))
    the_turtle.forward(40)

screen.exitonclick()
