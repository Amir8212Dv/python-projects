print("Welcome to tip calculator.")

bill = round(float(input("What was the total bill? $")), 2)

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people_count = int(input("How many people to split the bill? "))

total_bill = bill + bill * tip_percentage / 100

bill_per_person = round(total_bill / people_count, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")