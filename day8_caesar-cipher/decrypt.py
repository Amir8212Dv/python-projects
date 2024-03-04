from repo import letters


def decrypt():
    decrypt_input = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    def unshift_shifted_letter(
        character,
    ):
        if character not in letters:
            return character

        letter_index = letters.index(character) + 1

        unshifted_index = letter_index - shift_number + 26

        shifted_letter_index = unshifted_index - (26 * int(unshifted_index / 26))

        return letters[shifted_letter_index - 1]

    decrypted_text = ""

    for i in decrypt_input:
        decrypted_text += unshift_shifted_letter(i)

    print(f"Here's' your decoded result: {decrypted_text}")
