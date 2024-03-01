import random

letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
symbols = "!@#$%^&*()_+=-"
numbers = "0123456789"

print("Welcome to the PyPassword Generator!")

letters_count = int(input("How many letters do you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many number would you like?\n"))

password_characters = []

for i in range(letters_count):
    random_letter = random.choice(letters)
    password_characters.append(random_letter)

for i in range(symbols_count):
    random_symbol = random.choice(symbols)
    password_characters.append(random_symbol)

for i in range(numbers_count):
    random_number = random.choice(numbers)
    password_characters.append(random_number)

#! One way of creating password by random indexes
# password = ""
# for i in range(len(password_characters)):
#   random_number = random.randint(0 , len(password_characters) - 1)
#   password += password_characters.pop(random_number)

#! Better way to do it
random.shuffle(password_characters)
password = ''.join(password_characters)

print(f"Here is your password : {password}")
