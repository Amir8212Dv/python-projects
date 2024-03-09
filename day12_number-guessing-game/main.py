import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guess(turns):
    for i in range(1, 1 + turns):
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too High")
        elif guess < random_number:
            print("Too Low")
        else:
            print(f"You got it! The answer is {random_number}.\nGuess again.")
            return

        remained_attempt = turns - i
        if remained_attempt:
            print(f"You have {remained_attempt} attempt remaining to guess the number.")

    print("You've run out of guesses, you lose.")


while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        guess(EASY_LEVEL_TURNS)
        break
    elif difficulty == "hard":
        guess(HARD_LEVEL_TURNS)
        break
