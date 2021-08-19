print("Welcome to the tip calculator.")
bill = input("What was the total bill?")
perc = input("What percentage tip would you like to give? 10, 12, or 15?")
no_of_people = input("How many people to split the bill?")

amount_with_perc = float(bill) * (int(perc) / 100)
to_pay_amount = (float(bill) + amount_with_perc) / int(no_of_people)

total = "{:.2f}".format(to_pay_amount)
print(f"Each person should pay : {total}")
