from turtle import Turtle, Screen, colormode
from util import generate_random_rgb

the_turtle = Turtle("arrow")
the_turtle.speed("fastest")
the_turtle.pensize(1)
colormode(255)

screen = Screen()


number_of_circles = 120
circles_gap_size = 360 / number_of_circles  # It's an angle (ex: 3)

for i in range(number_of_circles):
    the_turtle.pencolor(generate_random_rgb())

    current_angle = (i - 1) * circles_gap_size
    next_angle = i * circles_gap_size - current_angle
    the_turtle.right(next_angle)
    the_turtle.circle(200)

screen.exitonclick()
