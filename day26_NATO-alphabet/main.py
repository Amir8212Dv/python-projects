import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

word = input("Enter word : ").upper()

spell = {letter: alphabet_data[alphabet_data.letter == letter].code.item() for letter in word}
print(spell)