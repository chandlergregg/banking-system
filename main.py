from Customer import Customer
from csv import reader
from time import sleep

def welcome_message():
    print(
        "==========================================\n"
        "---------- Welcome to PyBank! ------------\n"
        "==========================================\n"
    )

def log_in_menu():
    
    print(
        "Please enter an option below to login, create an account, or quit:\n"
        "(1) Log in\n"
        "(2) Create account\n"
        "(q) Quit\n"
    )
    customer = None
    while customer == None:
        
        login_option = input("Menu option: ")
        if login_option == "1":
            customer = log_in()
        elif login_option == "2":
            customer = create_account()
        # TODO: remove backdoor option for testing
        elif login_option == "3":
            customer = Customer("Ada", "Lovelace", "alovelace@gmail.com", "alovelace123")
        elif login_option == "q":
            break
        else:
            print(
                "\nPlease enter a valid menu option\n"
                "(1) Log in\n" 
                "(2) Create account\n"
                "(q) Quit\n"
            )
    
    return customer

def log_in():

    print("\nLogging in...")
    cust = None
    while cust == None:
        
        # Get input from customer and try to find login match
        email_address = input("Enter email address: ")
        password      = input("Enter password: ")
        cust = get_login_info(email_address, password)
        
        if cust is not None:
            print("Logged in!\n")
            return cust
        else:
            print("\nLogin unsuccessful. Please try again:")

def create_account():
    
    # Collect input from command line
    print("\nCreating account...")
    first_name      = input("Enter first name: ")
    last_name       = input("Enter last name: ")
    email_address   = input("Enter email address: ")
    password        = input("Enter password: ")
    tel_number      = input("Enter telephone number: ")

    # Create customer, save to csv, print, and return
    customer = Customer(first_name, last_name, email_address, password, tel_number)
    customer.save_to_csv("pybank_customers.csv")
    print(customer)
    return customer

def get_login_info(email_address, password):
    """
    Get login info for a given email address / pw combination.
    If login info does match, return customer object.
    If login info doesn't exist or doesn't match, return None.
    """
    # If email address and pw match records, return customer object, else return None
    with open("pybank_customers.csv", "r") as file:
        csvreader = reader(file)
        for line in csvreader:
            if line[2] == email_address and line[3] == password:
                return Customer(line[0], line[1], line[2], line[3], line[4])
    return None                 

def main_menu(customer):

    # loading_animation()
    print(f"\nWelcome to PyBank, {customer.first_name}.")
    print(f"How can we help you today?")
    
    menu_opt = None
    while menu_opt != "q":
    
        print(f"\nPlease select from the menu below:")
        print(
            "(1): Checking account\n"
            "(2): Savings account\n"
            "(3): Credit cards\n"
            "(4): Loans\n"
            "(q): Quit\n"
        )
        
        # Get menu input
        # If menu input is valid, call function. If quitting, break. Else re-prompt
        menu_opt = str(input("Menu option: "))
        menu = {
            "1": checking_menu,
            "2": savings_menu,
            "3": credit_card_menu,
            "4": loans_menu
        }
        menu_func = menu.get(menu_opt)
        if menu_func is not None:
            menu_func(customer)
        elif menu_opt == "q":
            quit_message(customer)
            break
        else:
            print("Invalid menu option. Please choose again.")
        
def checking_menu(customer):
    print("Checking account function")

def savings_menu(customer):
    print("Savings account function")

def credit_card_menu(customer):
    print("Credit card function")

def loans_menu(customer):
    print("Loans function")

def quit_message(customer):
    print(f"Thanks for banking with PyBank, {customer.first_name}!")

def loading_animation():
    for _ in range(25):
        print("$", end="", flush="True")
        sleep(.1)

## Start main part of program
welcome_message()
cust = log_in_menu()
if cust is not None:
    main_menu(cust)