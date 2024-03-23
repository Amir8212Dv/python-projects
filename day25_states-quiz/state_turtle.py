from turtle import Turtle


class StatesTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def add_state_name(self, name: str, position: tuple):
        self.goto(position)
        self.write(name, False, "center", ("Arial", 10, "normal"))
