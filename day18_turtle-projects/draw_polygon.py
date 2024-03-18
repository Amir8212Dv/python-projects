from turtle import Turtle, Screen
from util import generate_random_rgb

the_turtle = Turtle("arrow")
the_turtle.speed(5)
the_turtle.pu()
the_turtle.sety(450)
the_turtle.pd()
the_turtle.pensize(5)


for shape_sides_number in range(3, 10):
    the_turtle.color(generate_random_rgb())
    side_angle = 360 / shape_sides_number

    for i in range(shape_sides_number):
        the_turtle.right(side_angle)
        the_turtle.forward(200)


screen = Screen()
screen.exitonclick()
