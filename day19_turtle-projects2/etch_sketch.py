from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_right():
    turtle.right(10)


def turn_left():
    turtle.left(10)


def clear_screen():
    turtle.clear()


def reset_screen():
    screen.reset()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear_screen)
screen.onkeypress(key="r", fun=reset_screen)

screen.exitonclick()
