print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
peopleToSplit = int(input("How many people to split the bill? "))
percentageTip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

result = (totalBill + (totalBill*(percentageTip/100)))/peopleToSplit
print(f"Each person should pay: ${result:.1f}")
