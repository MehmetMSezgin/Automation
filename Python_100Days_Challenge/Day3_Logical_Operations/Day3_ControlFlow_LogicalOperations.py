a=10
if not a ==10 :
    print(1)
else:
    print(2)

def park():
    print("Welcome to the park")
    height = int(input("Height ? \n"))  # Assignment
    var = "Verified"

    if height == 120:  # Check equality
        print(f"{var}")
    elif 80 < height < 119 and height % 2 == 0:
        print(f"Almost, your number {height}")
    else:
        print("Rejected")

    if height != 120:
        print("Rejected")
    else:
        print(f"{var}")


# park()


def odd_or_even(number):
    if number != 0:
        if number % 2 == 0:
            print("even")
        elif number % 2 == 1:
            print("odd")
    else:
        print("Number 0")


# no = int(input("Number? \n "))
# odd_or_even(no)


def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f"{y} is a leap year")
            else:
                print(f"{y} is NOT a leap year")
        else:
            print(f"{y} is a leap year")
    else:
        print(f"{y} is NOT a leap year budy")


# input_data = int(input("Enter a year \n"))
# leap_year(input_data)


def python_pizza():
    print("Welcome to dashinka pizza")
    size = input("Select your size: S M L \n")
    size = size.capitalize()
    if size == "S" or size == "M" or size == "L":
        if size.capitalize() == "S":
            bill = 15
        elif size.capitalize() == "M":
            bill = 20
        elif size.capitalize() == "L":
            bill = 25

        print(f"You have selected {size} size pizza")
        peppe = input("Would you want pepperoni? Y/N ? \n ")
        peppe = peppe.capitalize()
        if peppe == "Y":
            if size == "M" or size == "L":
                bill += 3
            else:
                bill += 2

        cheese = input("Extra cheese ? Y/N \n")
        cheese = cheese.capitalize()
        if cheese == "Y":
            bill += 1
        print(f"Your bill: {bill} euro, please skip payment section")
    else:
        bill = 0
        print("size is not valid, order failed buddy")


python_pizza()
