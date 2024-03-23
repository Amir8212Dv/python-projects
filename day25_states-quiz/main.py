import pandas
import turtle
from state_turtle import StatesTurtle

data = pandas.read_csv("data/50_states.csv")

states_turtle = StatesTurtle()
screen = turtle.Screen()
screen.bgpic("data/blank_states_img.gif")
screen.title("U.S. States game")
screen.listen()

missing_states = data.state.tolist()
all_states_count = len(missing_states)


def exit_quiz():
    missing_states_data = data[data.state.isin(missing_states)]
    missing_states_data.to_csv("data/missing_states.csv")
    missing_states.clear()
    screen.bye()


while len(missing_states) != 0:
    user_input = screen.textinput(
        title=f"{all_states_count - len(missing_states)}/{all_states_count} States Correct",
        prompt="What's another state name?",
    ).title()
    if user_input == "Exit":
        exit_quiz()

    if user_input in missing_states:
        state_data = data[data.state == user_input]
        states_turtle.add_state_name(user_input, (int(state_data.x), int(state_data.y)))
        missing_states.remove(user_input)


screen.exitonclick()
