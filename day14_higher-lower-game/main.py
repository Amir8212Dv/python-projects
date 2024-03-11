from game_data import data
import random
from util import clear_lines
from logo import HIGHER_LOWER_LOGO,VS_LOGO

print(HIGHER_LOWER_LOGO)

def print_opponent_data(opponent):
    print("Compare A: {}, a {}, from {}".format(opponent["name"], opponent["description"], opponent["country"]))

def take_opponent():
    opponent_index = random.randint(0, len(data) - 1)
    opponent = data[opponent_index]
    del data[opponent_index]
    return opponent

def higher_lower_game(first_opponent=None, total_score=0):
    if first_opponent == None:
        first_opponent = take_opponent()
    second_opponent = take_opponent()

    print_opponent_data(first_opponent)
    print(VS_LOGO)
    print_opponent_data(second_opponent)

    user_chosen_opponent = first_opponent
    other_opponent = second_opponent
    while True:
        user_answer = input("Who has more followers on instagram? Type 'A' or 'B': ").lower()
        clear_lines(1)
        if user_answer == "b":
            user_chosen_opponent = second_opponent
            other_opponent = first_opponent
            break
        elif user_answer == "a":
            break

    if user_chosen_opponent["follower_count"] > other_opponent["follower_count"]:
        clear_lines(9 + int(bool(total_score)))
        print(f"You're right! Current score: {total_score + 1}")
        higher_lower_game(user_chosen_opponent, total_score + 1)
    else:
        clear_lines(9 + int(bool(total_score)))
        print(f"Sorry, that's wrong. Final score {total_score}")


higher_lower_game()
