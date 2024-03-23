import pandas
import turtle
from state_turtle import StatesTurtle

data = pandas.read_csv("50_states.csv")

states_turtle = StatesTurtle()
screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")
screen.title("U.S. States game")

available_states_list = data.state.tolist()
all_states_count = len(available_states_list)

while len(available_states_list) != 0:
    user_input = screen.textinput(
        title=f"{all_states_count - len(available_states_list)}/{all_states_count} States Correct",
        prompt="What's another state name?",
    ).title()
    if user_input in available_states_list:
        state_data = data[data.state == user_input]
        states_turtle.add_state_name(user_input, (int(state_data.x), int(state_data.y)))
        available_states_list.remove(user_input)


screen.exitonclick()
