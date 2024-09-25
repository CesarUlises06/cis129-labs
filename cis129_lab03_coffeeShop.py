"""
This program simulates a coffee shop, asks the number of coffees or muffins you want to buy, calculates price and tax
and prints a receipt
"""

# asks for number of coffees and muffins and convert string to integer

coffee = int(input("How many Coffees would you like?: "))
muffin = int(input("How many Muffins would you like?: "))

# multiply the amount of coffees ordered by 5 in order to get the price and assigns it to a variable

coffee_price = coffee * 5
muffin_price = muffin * 4

#  prints a receipt using f-strings to plug in input variables and newline characters for formatting

print("**********************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{coffee}")
print(f"Number of muffins bought?\n{muffin}")
print("**********************************\n")
print("**********************************")
print("My Coffee and Muffin Shop Receipt")

# using if-statements to check if number of items ordered is one and if it is it writes coffee/muffin non-plural

if coffee != 1:
    print(f"{coffee} Coffees at $5 each: ${coffee_price:.2f}")
else:
    print(f"{coffee} Coffee at $5 each: ${coffee_price:.2f}")  # using .2f to round till 2 decimal places

if muffin != 1:
    print(f"{muffin} Muffins at $4 each: ${muffin_price:.2f}")
else:
    print(f"{muffin} Muffin at $4 each: ${muffin_price:.2f}")

# calculating a 6% tax by adding the price of coffee and muffin together and multiplying by 0.06

tax = (coffee_price + muffin_price) * 0.06

# rounding the variable tax to 2 decimal places to not get super long floats using .2f20

print(f"6% tax: ${tax:.2f}")

# finishing receipt up, adding everything together to get final price

print("---------")
print(f"Total: ${coffee_price + muffin_price + tax:.2f}")
print("**********************************")
