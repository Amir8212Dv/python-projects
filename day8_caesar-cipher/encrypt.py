from repo import letters


def encrypt():
    plain_text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    def encrypt_letter(character):
        if character not in letters:
            return character

        letter_position = letters.index(character) + 1
        encrypted_letter_position = letter_position + shift_number
        encrypted_letter_index = encrypted_letter_position - (26 * int(encrypted_letter_position / 26)) - 1
        return letters[encrypted_letter_index]

    encrypted_text = ""
    for i in plain_text:
        encrypted_text += encrypt_letter(i)

    print(f"Here is your encoded result: {encrypted_text}")
