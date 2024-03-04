from repo import letters


def encrypt():
    decrypt_input = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    def pick_shifter_letter(character):
        if character not in letters:
            return character

        letter_index = letters.index(character)

        letter_index += 1

        shifted_index = letter_index + shift_number

        shifted_letter_index = shifted_index - (26 * int(shifted_index / 26))

        return letters[shifted_letter_index - 1]

    encrypted_text = ""

    for i in decrypt_input:
        encrypted_text += pick_shifter_letter(i)

    print(f"Here is your encoded result: {encrypted_text}")
