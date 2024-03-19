from turtle import Turtle, Screen
import random

screen = Screen()

screen_width = 1500
screen_height = 800
screen.setup(width=screen_width, height=screen_height, startx=0, starty=0)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

racers_count = 5
racers = []
racers_colors = ["red", "blue", "green", "orange", "purple"]

for i in range(racers_count):
    turtle_color = racers_colors[i]

    turtle = Turtle("turtle")
    turtle.color(turtle_color)
    turtle.shapesize(3)
    turtle.pu()
    turtle.setpos(-screen_width / 2 + 50, -200 + i * 100)

    racers.append({"turtle": turtle, "turtle_name": turtle_color})


winner_turtle = ""
while not winner_turtle:
    for racer in racers:
        racer["turtle"].forward(random.randint(50, 100))

        if racer["turtle"].xcor() >= (screen_width / 2 - 100):
            winner_turtle = racer["turtle_name"]
            break

print("RACE FINISHED")
if winner_turtle == user_bet:
    print("You Win")
else:
    print(f"You Lose! The winner turtle is {winner_turtle}")


screen.exitonclick()
