from logo import logo
from cards import cards, ace
import random
from util import clear_lines


def deal_card(hitter_cards):
    """Randomly choices a card and updates user or computer's cards list and points"""

    card = random.choice(cards)
    cards.remove(card)

    if card == ace:
        hitter_cards["ace_cards"].append(card)
    else:
        hitter_cards["non_ace_cards"].append(card)
    hitter_cards["all"].append(card)

    points = calculate_points(hitter_cards)

    return hitter_cards, points


def calculate_points(cards):
    """Calculates the total point"""

    points = sum(cards["non_ace_cards"])
    for _ in cards["ace_cards"]:
        if 11 + points > 21:
            points += 1
        else:
            points += 11
    return points


def print_table(user_cards, user_points, computer_cards, show_all=False):
    """Prints the all data that user needs to see"""

    clear_lines(3)
    user_all_cards = user_cards["all"]
    computer_all_cards = computer_cards["all"]

    print(f"Your cards: {user_all_cards}, current score: {user_points}")
    if show_all:
        print(f"Computer cards: {computer_all_cards}")
    else:
        print(f"Computer's first card: {computer_all_cards[0]}")


def blackjack():
    """Play one round of BlackJack"""

    print(logo)
    random.shuffle(cards)

    user_points = 0
    user_cards = {"non_ace_cards": [], "ace_cards": [], "all": []}
    for _ in range(2):
        user_cards, user_points = deal_card(user_cards)

    computer_points = 0
    computer_cards = {"non_ace_cards": [], "ace_cards": [], "all": []}
    for _ in range(2):
        computer_cards, computer_points = deal_card(computer_cards)

    if user_points == 21:
        print("\n$$ BLACKJACK $$\n")
        print_table(user_cards, user_points, computer_cards, True)
        return

    print_table(user_cards, user_points, computer_cards)

    while True:
        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_or_stand == "y":
            user_cards, user_points = deal_card(user_cards)
            if user_points > 21:
                print_table(user_cards, user_points, computer_cards, True)
                print("\n/\ LOSE /\\\n")
                return
            elif user_points == 21:
                print_table(user_cards, user_points, computer_cards, True)
                print("\n$$ BLACKJACK $$\n")
                return
            else:
                print_table(user_cards, user_points, computer_cards)

        elif hit_or_stand == "n":
            while computer_points < 17:
                computer_cards, computer_points = deal_card(computer_cards)

            print_table(user_cards, user_points, computer_cards, True)
            if computer_points > 21 or user_points > computer_points:
                print("\n** WIN **\n")
            elif user_points < computer_points:
                print("\n/\ LOSE /\\\n")
            elif user_points == computer_points:
                print("\n__ DRAW __\n")

            return
        else:
            clear_lines(1)


while input("Do you want to play another round of Blackjack? type 'y' or 'n': ") == "y":
    clear_lines(100)
    blackjack()
