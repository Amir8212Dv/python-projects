from util import clear_lines
from logo import logo

print(logo)
print("\n\nWelcome to the secrete auction program.\n\n")

bids = {}

while True:
    name = input("What is your name? ")
    bid = round(float(input("What's your bid? ")), 2)
    bids[name] = bid

    clear_lines(2)

    continue_or_not = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if continue_or_not == "no":
        break
    else:
        clear_lines(1)

highest_bid = max(bids)

print(f"The winner is {highest_bid} with a bid of ${bids[highest_bid]}")
