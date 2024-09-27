"""
This program simulates a coffee shop, asks the number of coffees, muffins, cake pops, and espressos you want to buy, calculates price and tax
and prints a receipt and gives a thank you message at the end
"""

# asks for number of items the user wants and convert string to integer

coffee = int(input("How many Coffees would you like?: "))
muffin = int(input("How many Muffins would you like?: "))
cake_pop = int(input("How many Cake Pops would you like?: "))
espresso = int(input("How many Espressos would you like?: "))

# multiplies the input variables by 5 in order to get the price and assigns it to a variable

coffee_price = coffee * 5
muffin_price = muffin * 4
cake_pop_price = cake_pop * 2
espresso_price = espresso * 3

#  prints a receipt using f-strings to plug in input variables and newline characters for formatting

print("\n**********************************")
print("My Coffee Shop")
print(f"Number of coffees bought?\n{coffee}")
print(f"Number of muffins bought?\n{muffin}")
print(f"Number of cake pops bought?\n{cake_pop}")
print(f"Number of espressos bought?\n{espresso}")
print("**********************************\n")
print("**********************************")
print("My Coffee Shop Receipt")

# using if-statements to check if number of items ordered is 1 and if it is it writes coffee/muffin non-plural

if coffee != 1:
    print(f"{coffee} Coffees at $5 each: ${coffee_price:.2f}")
else:
    print(f"{coffee} Coffee at $5 each: ${coffee_price:.2f}")  # using .2f to round till 2 decimal places

if muffin != 1:
    print(f"{muffin} Muffins at $4 each: ${muffin_price:.2f}")
else:
    print(f"{muffin} Muffin at $4 each: ${muffin_price:.2f}")

if cake_pop != 1:
    print(f"{cake_pop} Cake Pops at $2 each: ${cake_pop_price:.2f}")
else:
    print(f"{cake_pop} Cake Pop at $2 each: ${cake_pop_price:.2f}")

if espresso != 1:
    print(f"{espresso} Espressos at $3 each: ${espresso_price:.2f}")
else:
    print(f"{espresso} Espresso at $3 each: ${espresso_price:.2f}")

# calculating a 6% tax by adding the price of everything ordered and multiplying by 0.06

tax = (coffee_price + muffin_price + cake_pop_price + espresso_price) * 0.06

# rounding the variable, tax to 2 decimal places to not get super long floats using .2f

print(f"6% tax: ${tax:.2f}")

# finishing receipt up, adding everything together to get final price

print("---------")
print(f"Total: ${coffee_price + muffin_price + cake_pop_price + espresso_price + tax:.2f}")
print("**********************************")

# printing a thank-you message and using a newline character for a blank line

print("\nThank you, come again soon!")
