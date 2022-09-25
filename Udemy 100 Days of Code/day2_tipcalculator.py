print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? ")) / 100 + 1
split = int(input("How many people to split the bill? "))
total = bill * tip / split
total_2dp = "{:.2f}".format(total)
print(f"Each person has to pay ${total_2dp}")