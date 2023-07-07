# import files
# while loop create
# retrieve data (50)
# compare verify
# if guess true a becomes b and retrieve new data
# else calculate total point and over the game

from Day14_HigherLowerArt import logo, vs
from Day14_GameData import data
import random

print(len(data))
flag = True
point_counter = 0
list_number_A = random.randint(0, 49)
list_number_B = random.randint(0, 49)

while flag:
    print(logo)

    a_name = data[list_number_A].get("name")
    a_description = data[list_number_A].get("description")
    a_country = data[list_number_A].get("country")
    a_follower = data[list_number_A].get("follower_count")

    b_name = data[list_number_B].get("name")
    b_description = data[list_number_B].get("description")
    b_country = data[list_number_B].get("country")
    b_follower = data[list_number_B].get("follower_count")

    print(f'Compare A: {a_name}, {a_description}, {a_country} .')
    print(vs)
    print(f'Againist B: {b_name}, {b_description}, {b_country} .')

    user_selection = input("Who has more followers. Type 'A' or 'B' \n").upper()

    if (user_selection == "A" and a_follower >= b_follower) or (user_selection == "B" and b_follower >= a_follower):
        point_counter += 1
        print(f'Your current point is {point_counter} ')
        print(f'Correct ! followers are {a_follower} , {b_follower}')
        list_number_A = list_number_B
        list_number_B = random.randint(0, 49)
    else:
        print(point_counter)
        print(f'You LOST ! followers are {a_follower} , {b_follower}')
        print(f'Your final point is {point_counter} ')
        flag = False

'''
Angela's solution

from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()




# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

'''


