import random
from Day12_NumberGuessingArt import logo

my_variable = 1


def increase_num():
    '''In order to use gloabal variable in def , it needs to be defined as global in the beginning of def'''
    global my_variable
    my_variable += 1


'''It not suggested to modify gloabal variable inside of def'''


def number_guess():
    print(logo)
    print("Welcome to number guess game")
    attempt = 3
    number = random.randint(1, 10)

    while attempt > 0:
        print(f"{attempt} attempt left")
        guess = int(input("Please guess a number between 1-10 \n"))

        if number == guess:
            print("Jackpot!")
            exit()
        elif guess > number:
            print("Too high")
            attempt -= 1
        elif number > guess:
            print("Too low")
            attempt -= 1

    if attempt > 0:
        print("You Won !")
    else:
        print("You Lost !")
        print(f"Number is {number}")


number_guess()
