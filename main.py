MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Dictionary for resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Dictionary with the unit by resource
units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",

}

# Dictionary with the coins
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

# Global Variables
money = 0
turnoff_machine = False


# Function definitions
def print_report():
    """Print the resources along with the corresponding units"""
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}{units[key]}")
    print(f"Money: ${money}")


def check_resources(coffee):
    """Check if there is enough resource for the coffee. Return True otherwise."""
    list_coffee = MENU[coffee]['ingredients']
    for key in list_coffee:
        if resources[key] < MENU[coffee]['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    """Ask user for coins and calculate the amount_paid"""
    payment = 0
    print("Please insert coins.")
    for key in coins:
        qty = int(input(f"how many {key}?: "))
        payment += qty * coins[key]
    return payment


def check_payment(coffee_price, amount_paid):
    """Check if the amount of money is enough to make the coffee"""
    if amount_paid < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        refund = amount_paid - coffee_price
        if refund > 0:
            print(f"Here is ${refund:.2f} dollars in change.")
    return True


def reduce_inventory(coffee):
    """reduce the amount needed to make coffee from the resources"""
    list_coffee = MENU[coffee]['ingredients']
    for key in list_coffee:
        resources[key] -= list_coffee[key]


while not turnoff_machine:
    option = input("    What would you like? (espresso/latte/cappuccino): ").lower()

    # Check option selected by user and call function accordingly
    if option == 'off':
        # The program ends. Set variable to True
        turnoff_machine = True
    elif option == 'report':
        # print the report by calling the function
        print_report()
    elif option in MENU:
        # Check if there is enough resources to make coffee
        if check_resources(option):
            money_paid = process_coins()
            # Get coffee price
            coffee_cost = MENU[option]['cost']
            if check_payment(coffee_cost, money_paid):
                money += coffee_cost
                reduce_inventory(option)
                print(f"Here is your {option} ☕. Enjoy!")
    else:
        print("Sorry there is no such a coffee in this machine.")
