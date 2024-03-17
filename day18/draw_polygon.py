from turtle import Turtle, Screen

the_turtle = Turtle("arrow")
the_turtle.color("black")
the_turtle.pu()
the_turtle.sety(450)
the_turtle.pd()
the_turtle.speed(5)

colors = [
    "blue",
    "green",
    "red",
    "yellow",
    "orange",
    "brown",
    "black",
]
the_turtle.pensize(5)

for shape_sides_number in range(3, 10):
    the_turtle.color(colors[shape_sides_number - 3])
    side_angle = 360 / shape_sides_number

    for i in range(shape_sides_number):
        the_turtle.right(side_angle)
        the_turtle.forward(200)


screen = Screen()
screen.exitonclick()
