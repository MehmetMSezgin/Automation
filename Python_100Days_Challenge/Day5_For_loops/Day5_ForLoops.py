import random

numbers = [1, 2, 3]
for number in numbers:
    print(number)

print('------------------------------')


def for_loops_in_range():
    for number in range(1, 10):
        print(number)

    print("-----------------")
    for odd_numbers in range(1, 10, 2):
        print(odd_numbers)


# for_loops_in_range()


def height_generator():
    my_list = input("Enter the list of height\n")
    my_list = my_list.split(" ")
    print(my_list)
    total_height = 0
    number_of_person = 0
    my_int_list = []
    for i in my_list:
        total_height += int(i)
        number_of_person += 1
        my_int_list.append(int(i))

    print(sum(my_int_list))
    print(max(my_int_list))
    result = total_height / number_of_person
    print(result)


# height_generator()

def fizzbuzz():
    for i in range(1, 50):
        if i % 3 == 0 and not i % 5 == 0:
            print("fizz")
        elif i % 5 == 0 and not i % 3 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            print(i)


# fizzbuzz()

letters = ["a", "b", "c", "d", "e", "m", "k", "l", "z", "o"]
symbols = ["¤", "&", "%", "*", "#"]
numbers = ["1", "2", "3", "4", "5", "6"]


def password_generator():
    print("Welcome to password generator")
    input_letters = int(input("How many letters ?\n"))
    input_symbols = int(input("How many symbols ?\n"))
    input_numbers = int(input("How many numbers ?\n"))
    password = ""
    if not input_letters == 0 and not input_symbols == 0 and not input_numbers == 0:
        for i in range(1, (input_numbers + 1)):
            i = random.choice(numbers)  # random choice
            password += i
        for j in range(1, (input_letters + 1)):
            j = random.choice(letters)
            password += j
        for x in range(1, (input_symbols + 1)):
            x = random.choice(symbols)
            password += x
    else:
        print("Cannot provide password")

    print(password)
    shuffled_password = "".join(random.sample(password, len(password)))
    print(f"Your password is {shuffled_password}")


password_generator()
