resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

def check_resources(drink):
    for ingredient in menu[drink]["ingredients"]:
        if resources[ingredient] < menu[drink]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_amount = quarters + dimes + nickels + pennies
    if total_amount < menu[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total_amount > menu[drink]["cost"]:
        change = round(total_amount - menu[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
    return True

def make_coffee(drink):
    for ingredient in menu[drink]["ingredients"]:
        resources[ingredient] -= menu[drink]["ingredients"][ingredient]
    resources["money"] += menu[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")

def print_report():
    print("Current Resources:")
    for resource, amount in resources.items():
        if resource != "money":
            print(f"{resource.capitalize()}: {amount}ml")
        else:
            print(f"{resource.capitalize()}: ${amount}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    elif choice in menu:
        if check_resources(choice):
            if process_coins(choice):
                make_coffee(choice)
    else:
        print("Invalid input. Please try again.")
