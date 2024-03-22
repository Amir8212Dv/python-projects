with open("./Letters/starting_letter.txt") as file:
    base_letter = file.read()

with open("./Names/invited_names.txt") as file:
    names = file.read()

separate_names = names.split("\n")
for name in separate_names:
    updated_letter = base_letter.replace("[name]", name)
    with open(f"./Letters/{name}.txt", "w") as file:
        file.write(updated_letter)
