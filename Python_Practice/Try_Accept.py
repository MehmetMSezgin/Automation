try:
    #value = 10/0
    number = int(input("enter a number "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("!!zero")


##print out error
try:
    number = int(input("enter a number "))
    print(number)
except ValueError as errorsSource:
    print(errorsSource)
