# Module 4 lab-4
# Cesar Ulises Valenzuela
# October 10, 2024
# My program

# main function

def main():
    """declares local variables"""
    monthly_sales = 120500
    store_amount = 6000
    emp_amount = 75
    sales_increase = 0.05
    # calls all the functions with correct parameters
    get_sales(prompt_2)
    get_increase(prompt)
    calc_store_bonus(monthly_sales)
    calc_emp_bonus(sales_increase)
    print_bonus(store_amount, emp_amount)




prompt = "Please enter the percent of sales increase: "
prompt_2 = "Please enter the monthly sales: "
# This function gets the monthly sales

def get_sales(prompt_2):
    monthly_sales = float(input(prompt_2))
    return monthly_sales

# This function gets the percent of increase in sales

def get_increase(prompt):
    sales_increase = float(input(prompt))
    sales_increase = sales_increase / 100
    return sales_increase

# This function determines the store_amount bonus

def calc_store_bonus(monthly_sales):
    if monthly_sales >= 110000:
        store_amount = 6000
    elif monthly_sales >= 100000:
        store_amount = 5000
    elif monthly_sales >= 90000:
        store_amount = 4000
    elif monthly_sales >= 80000:
        store_amount = 3000
    else:
        store_amount = 0

    return store_amount

# This function determines the emp_amount bonus

def calc_emp_bonus(sales_increase):
    if sales_increase >= 5:
        emp_amount = 75
    elif sales_increase >= 4:
        emp_amount = 50
    elif sales_increase >= 3:
        emp_amount = 40
    else:
        emp_amount = 0

    return emp_amount

# This function prints the bonus information

def print_bonus(store_amount, emp_amount):
    print(f"The store bonus amount is ${store_amount}")
    print(f"The employee bonus amount is ${emp_amount}")
    if store_amount == 6000 and emp_amount == 75:
        print("Congrats! you have reached the highest bonus amounts possible! ")

# calls main function
main()
