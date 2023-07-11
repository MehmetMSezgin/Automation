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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_on_off = True
current_water = resources.get("water")
current_milk = resources.get("milk")
current_coffee = resources.get("coffee")
money_in_case = 0


def payment(choice):
    coins = float(input("Please insert coins \n One coin 0.25 cent \n"))
    money_amount = coins * 0.25
    coffe_price = float(MENU.get(choice).get("cost"))
    print(f"Given money {money_amount}")
    print(f"Selected coffee price {coffe_price}")

    if money_amount < coffe_price:
        print("Insufficient amount !")
        exit()

    refund = money_amount - coffe_price
    return refund


while turn_on_off:
    user_choice = input("☕ What would you like? \n espresso(1) \n latte(2) \n cappuccino(3) \n "
                        "Turn off machine(off) \n report \n ")

    if user_choice == "off":
        print("Shutting down...")
        exit()

    if user_choice == "report":
        print(resources)
        print(money_in_case)

    if user_choice == "1":
        if current_water > 50 and current_coffee > 18:
            refund_amount = payment("espresso")
            money_in_case = money_in_case + 1.5
            current_coffee = current_coffee - int(MENU.get("espresso").get("ingredients").get("coffee"))
            current_water = current_water - int(MENU.get("espresso").get("ingredients").get("water"))
            print("Your coffee is preparing . . .")
            print(" READY ! ! !")
            print(f"Your refund {refund_amount}")

        else:
            print("There is not enough resources")
            turn_on_off = False

    if user_choice == "2":
        if current_water > 200 and current_milk > 150 and current_coffee > 24:
            refund_amount = payment("latte")
            money_in_case = money_in_case + 2.5
            current_coffee = current_coffee - int(MENU.get("latte").get("ingredients").get("coffee"))
            current_water = current_water - int(MENU.get("latte").get("ingredients").get("water"))
            current_milk = current_milk - int(MENU.get("latte").get("ingredients").get("milk"))
            print("Your coffee is preparing . . .")
            print(" READY ! ! !")
            print(f"Your refund {refund_amount}")
        else:
            print("There is not enough resources")
            turn_on_off = False

    if user_choice == "3":
        if current_water > 250 and current_milk > 100 and current_coffee > 24:
            refund_amount = payment("cappuccino")
            money_in_case = money_in_case + 3
            current_coffee = current_coffee - int(MENU.get("cappuccino").get("ingredients").get("coffee"))
            current_water = current_water - int(MENU.get("cappuccino").get("ingredients").get("water"))
            current_milk = current_milk - int(MENU.get("cappuccino").get("ingredients").get("milk"))
            print("Your coffee is preparing . . .")
            print(" READY ! ! !")
            print(f"Your refund {refund_amount}")

        else:
            print("There is not enough resources")
            turn_on_off = False
