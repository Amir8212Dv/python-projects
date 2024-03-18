from turtle import Turtle, Screen, colormode
import random


the_turtle = Turtle("arrow")
the_turtle.speed("fastest")
the_turtle.pensize(15)
colormode(255)

screen = Screen()

def generate_random_rgb():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    return r,g,b

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
