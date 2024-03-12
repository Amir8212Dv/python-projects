from game_data import data
import random
from util import clear_lines
from logo import HIGHER_LOWER_LOGO, VS_LOGO

print(HIGHER_LOWER_LOGO)


def print_account_data(account, account_flag):
    print(
        "Compare {}: {}, a {}, from {}".format(
            account_flag, account["name"], account["description"], account["country"]
        )
    )


def take_account():
    account_index = random.randint(0, len(data) - 1)
    account = data[account_index]
    del data[account_index]
    return account


def higher_lower_game(first_account=None, total_score=0):
    if first_account == None:
        first_account = take_account()
    second_account = take_account()

    print_account_data(first_account, "A")
    print(VS_LOGO)
    print_account_data(second_account, "B")

    user_chosen_account = first_account
    other_account = second_account
    while True:
        user_answer = input("\n\nWho has more followers on instagram? Type 'A' or 'B': ").lower()
        clear_lines(3)
        if user_answer == "b":
            user_chosen_account = second_account
            other_account = first_account
            break
        elif user_answer == "a":
            break

    if user_chosen_account["follower_count"] > other_account["follower_count"]:
        clear_lines(9 + int(bool(total_score)))
        print(f"You're right! Current score: {total_score + 1}")
        higher_lower_game(second_account, total_score + 1)
    else:
        clear_lines(9 + int(bool(total_score)))
        print(f"Sorry, that's wrong. Final score {total_score}")


higher_lower_game()
