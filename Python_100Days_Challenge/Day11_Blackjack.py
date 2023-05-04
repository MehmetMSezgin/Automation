############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer
import random
from Day11_BlackjackArt import logo


def drawAnotherCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_no = cards[random.randint(0, 12)]
    return card_no


def blackjack():
    flag = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(logo)

    user_first_card = cards[random.randint(0, 12)]
    print(f"Your first card is {user_first_card}")

    dealer_first_card = cards[random.randint(0, 12)]
    print(f"Dealer's first card is {dealer_first_card}")

    user_second_card = cards[random.randint(0, 12)]
    print(f"Your second card is {user_second_card}")

    if user_second_card == 11:
        which_1_or_11 = input("Would you prefer 1 or 11")
        if which_1_or_11 == 1:
            user_second_card = 1
        elif which_1_or_11 == 11:
            user_second_card = 11

    dealer_second_card = cards[random.randint(0, 12)]

    user_total_score = user_first_card + user_second_card
    dealer_total_score = dealer_first_card + dealer_second_card

    while flag:
        user_answer = input("Hit card y/n? \n")

        if user_answer == "n":
            print(f"Your score: {user_total_score}")
            print(f"Dealer score: {dealer_total_score}")

            if user_total_score > 21:
                return 2

            while dealer_total_score < 16:
                print("Dealer's score is less than 16. Drawing a card...")

                add_card = drawAnotherCard()
                dealer_total_score += add_card

                print("************ New scores ************")
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")

            if user_total_score > dealer_total_score:
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")
                return 1
            elif user_total_score < dealer_total_score:
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")
                return 2
            elif user_total_score == dealer_total_score:
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")
                return 0
            flag = False
        elif user_answer == "y":
            print(f"Your score: {user_total_score}")
            print(f"Dealer score: {dealer_first_card} + X")

            if user_total_score > 21:
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")
                return 2

            add_new_card = drawAnotherCard()
            print(f"Your new card is {add_new_card}")

            user_total_score += add_new_card

            print("------ NEW SCORES --------")
            print(f"Your score: {user_total_score}")
            print(f"Dealer score: {dealer_first_card} + X")

            if user_total_score > 21:
                print(f"Your score: {user_total_score}")
                print(f"Dealer score: {dealer_total_score}")
                return 2




play = blackjack()
if play == 1:
    print("You won ! ! !")
elif play == 2:
    print("You lost ! ! !")
elif play == 0:
    print("Draw")
