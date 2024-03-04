from encrypt import encrypt
from decrypt import decrypt

while True:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if action == "encode":
        encrypt()
    elif action == "decode":
        decrypt()
    else:
        print("Please enter  'encode' or 'decode'")
        continue

    ask_to_repeat = input("Type 'yes' if you want to go again. Other. Otherwise type 'no'\n").lower()

    if ask_to_repeat != "yes":
        break
