# Module 4 Lab-4
# Ricardo Ochoa
# 2/19/2924
# This is a program discription

# declare local variables
monthlySales = 0  # monthly sales amount
storeamount= 0  # store bonus amount
empAmount = 0  # employee bonus amount
employee bonus ease = 0  # percent of sales increase
prompt = Enter the monthly sales amount: # prompt will be a string literal

    

# This code gets the monthly sales

monthlySales = float(input(prompt))

# This code determines the store bonus

if monthlySales >= 110000:
	storeAmount = 6000
elif _monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
	storeAmount = 0



# This code gets the percent of increase in sales
salesIncrease = float(input(Enter percent of sales increase:))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount =50
elif salesIncrease >= .03:

	empAmount = 40
else:
	empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $",storeamount)
print("The employee bonus amount is $", empAmount)
if (storeamount == 6000 ) and (empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible! ')
