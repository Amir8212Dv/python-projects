import signs
import random

options = [["rock", signs.rock], [
    "paper", signs.paper], ["scissors", signs.scissors]]

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input > 3 or user_input < 0:
    print("Try again and enter a valid number (0 , 1 , 2)")
    quit()

user_choice = options[user_input]
computer_choice = options[random.randint(0, 2)]

print(user_choice[1])
print(f"Computer choice :\n{computer_choice[1]}")

outcome = ""

lose_message = "You lose"
win_message = "You win"
draw_message = "Draw"

if user_choice[0] == computer_choice[0]:
    outcome = draw_message
elif user_choice[0] == "rock":
    if computer_choice[0] == "paper":
        outcome = lose_message
    else:  # scissors
        outcome = win_message
elif user_choice[0] == "paper":
    if computer_choice[0] == "rock":
        outcome = win_message
    else:  # scissors
        outcome = lose_message
elif user_choice[0] == "scissors":
    if computer_choice[0] == "rock":
        outcome = lose_message
    else:  # paper
        outcome = win_message

print(outcome)
