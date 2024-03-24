numbers = [[1], [1, 1]]
steps = int(input("How many steps? "))

for _ in range(steps):
    new_numbers = [1, 1]
    for i in range(1, len(numbers[-1])):
        new_numbers.insert(i, numbers[-1][i] + numbers[-1][i - 1])
    numbers.append(new_numbers)

longest_len = len(str(numbers[-1]))
for i in range(len(numbers)):
    item = numbers[i]
    diff = int((longest_len - len(str(item))) / 2)
    log_string = str(item).replace(",", "     ").replace("[", "").replace("]", "")
    print(" " * (diff + len(numbers) - i), log_string , "\n")
