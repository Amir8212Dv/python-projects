from turtle import Turtle, Screen, colormode
from util import generate_random_rgb


the_turtle = Turtle("circle")
screen = Screen()

the_turtle.speed("fastest")
colormode(255)


dots_in_row = 10
dots_gap = 80
dot_size = 30

# Centering the painting:
the_turtle.pu()
the_turtle.right(90)
the_turtle.forward(dots_in_row * dots_gap / 2 - dot_size)
the_turtle.right(90)
the_turtle.forward(dots_in_row * dots_gap / 2 - dot_size)
the_turtle.right(180)


def draw_dot():
    the_turtle.pd()
    the_turtle.dot(dot_size, generate_random_rgb())


for i in range(dots_in_row):
    for j in range(dots_in_row - 1):
        draw_dot()
        the_turtle.pu()
        the_turtle.forward(dots_gap)

    # Draw last dot in line
    draw_dot()
    the_turtle.pu()

    # Move to next line
    turtle_heading = the_turtle.heading()
    the_turtle.setheading(90)
    the_turtle.forward(dots_gap)
    the_turtle.setheading(180 - turtle_heading)


the_turtle.hideturtle()
screen.exitonclick()
