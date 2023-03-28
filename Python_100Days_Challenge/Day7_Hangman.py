import random
import Day7_Hangman_world_list
from  Day7_Hangman_Art import logo,stages

print(logo)

#world_list = ["mouse", "table", "cat", "car", "wall", "plane", "dictionary", "corporation", "library"]

chosen_word = random.choice(Day7_Hangman_world_list.word_list)
#print(chosen_word)

length_of_word = len(chosen_word)
#print(length_of_word)

screen = []
for i in range(0, length_of_word):
    screen.append("_")

print(screen)

chosen_word_as_list = []
for i in range(length_of_word):
    chosen_word_as_list.append(chosen_word[i])
#print(chosen_word_as_list)

flag = False
lives = 6

while not flag:
    user_input = (input("Please guess a word\n")).lower()

    if len(user_input) != 1:
        print("Invalid choice game is reset")
        exit()

    if user_input in screen:
        print(f"You have already guessed {user_input}")

    counter = 0
    for i in range(0, length_of_word):
        if chosen_word[i] == user_input:
            screen[i] = user_input
        else:
            counter = counter+1

    if counter == length_of_word:
        print(stages[lives])
        print("Wrong!")
        lives -= 1

    if lives == -1:
        flag = True
        print("You LOST!!!")
        print(f"The word was {chosen_word_as_list}")

    if chosen_word_as_list == screen:
        flag = True
        print("You WON !!!")

    print(screen)
