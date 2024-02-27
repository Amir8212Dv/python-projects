import signs
import random

options = [["Rock" , signs.rock] , ["Paper" , signs.paper], ["Scissors" , signs.scissors]]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

user_choice = options[user_input]
computer_choice = options[random.randint(0,2)]

print(user_choice[1])
print(f"Computer choice :\n{computer_choice[1]}")

outcome = ""

lose_message = "You lose"
win_message = "You win"
draw_message = "Draw"

if user_choice[0] == computer_choice[0]:
  outcome = draw_message
elif user_choice[0] == "Rock":
  if computer_choice[0] == "Paper":
    outcome = lose_message
  else: #Scissors
    outcome = win_message
elif user_choice[0] == "Paper":
  if computer_choice[0] == "Rock":
    outcome = win_message
  else: #Scissors
    outcome = lose_message
elif user_choice[0] == "Scissors":
  if computer_choice[0] == "Rock":
    outcome = lose_message
  else : #Paper
    outcome = win_message

print(outcome)