income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
 income > 85528
 tax = 14.839 * 0.32 # Write the rest of your code here.

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 