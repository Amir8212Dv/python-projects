import repo
import random
import sys

print(repo.HANGMAN_LOGO)

def remove_last_n_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line

random_word = list(random.choice(repo.words))
random_word_length = len(random_word)
user_choices = list("_" * random_word_length)
hangman_step = 0

while True:
    remove_last_n_lines(1)
    print(" ".join(user_choices))

    user_guess = input('Choose a letter : ').lower()

    if user_guess in random_word and user_guess not in user_choices:
        for i in range(random_word_length):
            if random_word[i] == user_guess:
                user_choices[i] = user_guess

        if ("".join(user_choices) == random_word):
            print("YOU WIN")
            break
    else:
        hangman_step += 1

    if hangman_step:
        remove_last_n_lines(9)
        print(repo.HANGMAN_PICS[hangman_step])

        if (hangman_step == len(repo.HANGMAN_PICS) - 1):
            print("YOU LOSE")
            break
    else:
        remove_last_n_lines(1)  # Only runs once in the first loop
