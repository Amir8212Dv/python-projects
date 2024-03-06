from repo import letters


def decrypt():
    encrypted_text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    def unshift_encrypted_letter(character):
        if character not in letters:
            return character

        letter_position = letters.index(character) + 1
        decrypted_letter_position = letter_position - shift_number
        decrypted_letter_index = (decrypted_letter_position % 26) - 1
        return letters[decrypted_letter_index]

    decrypted_text = ""
    for i in encrypted_text:
        decrypted_text += unshift_encrypted_letter(i)

    print(f"Here's' your decoded result: {decrypted_text}")
