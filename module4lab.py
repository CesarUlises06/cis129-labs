# Module 4 lab-4
# Cesar Ulises Valenzuela
# October 16, 2024
"""
My program calculates the store bonus amount and the employee bonus amount based off the monthly sales
and the percent of sales increase entered in by the user
"""

# Main function
def main():
    """Declares local variables and calculates bonuses based on sales data"""
    monthly_sales = get_sales(prompt_2)
    sales_increase = get_increase(prompt)
    store_amount = calc_store_bonus(monthly_sales)
    emp_amount = calc_emp_bonus(sales_increase)
    print_bonus(store_amount, emp_amount)

prompt = "Please enter the percent of sales increase: "
prompt_2 = "Please enter the monthly sales: "


def get_sales(prompt_2):
    """Gets the monthly sales from user input"""
    monthly_sales = float(input(prompt_2))
    return monthly_sales


def get_increase(prompt):
    """Gets the percent increase in sales from user input and converts it to a decimal"""
    sales_increase = float(input(prompt))
    sales_increase = sales_increase / 100
    return sales_increase


def calc_store_bonus(monthly_sales):
    """Determines the store bonus amount based on monthly sales"""
    if monthly_sales >= 110000:
        return 6000
    elif monthly_sales >= 100000:
        return 5000
    elif monthly_sales >= 90000:
        return 4000
    elif monthly_sales >= 80000:
        return 3000
    else:
        return 0


def calc_emp_bonus(sales_increase):
    """Determines the employee bonus amount based on sales increase"""

    if sales_increase >= 0.05:  # Compare to decimal values
        return 75
    elif sales_increase >= 0.04:
        return 50
    elif sales_increase >= 0.03:
        return 40
    else:
        return 0


def print_bonus(store_amount, emp_amount):
    """Prints the store and employee bonus amounts"""

    print(f"The store bonus amount is $ {store_amount}")  # Added space between $ and amount
    print(f"The employee bonus amount is $ {emp_amount}")  # Added space between $ and amount
    if store_amount == 6000 and emp_amount == 75:
        print("Congrats! You have reached the highest bonus amounts possible!")  # Ensure this message is on one line

# Calls main function
main()
