class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: "RealProperty"):  # !!! Inside of quotes !!!
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False


if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))


# ---------------------------
# ===========================
# ---------------------------
# Passing one class to another as argument
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount


if __name__ == "__main__":
    exactum = PaymentTerminal()
    card = LunchCard(2)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")


# ---------------------------
# ===========================
# ---------------------------

# encapsulation
class CreditCard:
    # the attribute number is private, while the attribute name is accessible
    def __init__(self, number: str, name: str):
        self.__number = number
        self.name = name


# getters setters
class Wallet:
    def __init__(self):
        self.__money = 0

    # A getter method
    @property  # the getter method, i.e. the @property decorator, must be introduced before the setter method,
    # or there will be an error when the class is executed.
    def money(self):
        return self.__money

    # A setter method
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money


# usage
wallet = Wallet()
print(wallet.money)

wallet.money = 50  # paranthesis is not necessary
print(wallet.money)


# ---------------------------
# ===========================
# ---------------------------
# default values of parameters
class Student:
    """ This class models a student """

    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = ""):
        # calling the setter method for the name attribute
        self.name = name


# ---------------------------
# Inheritance
# ---------------------------
class Book:
    """ This class models a simple book """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class BookContainer:
    """ This class models a container for books """

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
    """ This class models a shelf for books """

    def __init__(self):
        super().__init__()  # It uses BookContainer init

    def add_book(self, book: Book, location: int):  # Overriding !!!
        self.books.insert(location, book)


# ---------------
# what if all attributes are not identical
class Book:
    """ This class models a simple book """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class Thesis(Book):
    """ This class models a graduate thesis """

    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade


# ---------------------------
# Overloading operators
# ---------------------------
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def __gt__(self, another_product):  # returns true or false
        return self.price > another_product.price


# implementation
orange = Product("Orange", 2.90)
apple = Product("Apple", 3.95)

if orange > apple:
    print("Orange is greater")
else:
    print("Apple is greater")


# __repr__
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"  # it uses {repr(self.name)} ?

    def __str__(self):
        return f"{self.name} ({self.age} years)"


# example
Person = Person("Anna", 25)
print(Person)  # Anna (25 years)
print(repr(Person))  # Person('Anna', 25)

persons = []
persons.append(Person("Anna", 25))
persons.append(Person("Peter", 99))
persons.append(Person("Mary", 55))
print(persons)  # [Person('Anna', 25), Person('Peter', 99), Person('Mary', 55)]


# ---------------------------
# Quote issue , when passing class object into same class
# ---------------------------
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: 'Money'):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        else:
            return False


'''
Explanation:

Quotes ('Money'): Using quotes allows you to reference a class that is defined later in the code or in a different module. This is called a forward reference.
In this case, it helps if the Money class is used before its actual definition is processed by the interpreter.

Without Quotes (Money): If you use the class directly without quotes, it works as long as the Money class is already defined when the type hint is processed.
'''

# ---------------
# Join
# ----------------
name = "Peter"
char_list = list(name)
print(char_list)

print("".join(char_list))
print(" ".join(char_list))
print(",".join(char_list))
print(" and ".join(char_list))


# ----------
# Sort objects
# ----------
class Student:
    """ The class models a single student """

    def __init__(self, name: str, id: str, credits: int):
        self.name = name
        self.id = id
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.id}), {self.credits} cr."


def by_id(item: Student):
    return item.id


def by_credits(item: Student):
    return item.credits


if __name__ == "__main__":
    o1 = Student("Archie", "a123", 220)
    o2 = Student("Marvin", "m321", 210)
    o3 = Student("Anna", "a999", 131)

    students = [o1, o2, o3]

    print("Sort by id:")
    for student in sorted(students, key=by_id):
        print(student)

    print()

    print("Sort by credits:")
    for student in sorted(students, key=by_credits):
        print(student)

# -----------
# Another example

for player in sorted(team_player_list, key=lambda player: player['name']):  # sort by name
    total = player['goals'] + player['assists']
    print(f"{player['name']:21}{player['team']:3}{player['goals']:4} + {player['assists']:2} = {total:3}")


# ------------
# MAP
# -----------
class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1000000)

accounts = [a1, a2, a3]

clients = map(lambda t: t.name, accounts)
for name in clients:
    print(name)

balances = map(lambda t: t.get_balance(), accounts)
for balance in balances:
    print(balance)

# -----------
# Reduce
# -----------
from functools import reduce

my_list = [2, 3, 1, 5]


# a helper function for reduce, adds one value to the current reduced sum
def sum_helper(reduced_sum, item):
    print(f"the reduced sum is now {reduced_sum}, next item is {item}")
    # the new reduced sum is the old sum + the next item
    return reduced_sum + item


sum_of_numbers = reduce(sum_helper, my_list, 0)

print(sum_of_numbers)

"""
The program prints out:
Sample output
the reduced sum is now 0, next item is 2
the reduced sum is now 2, next item is 3
the reduced sum is now 5, next item is 1
the reduced sum is now 6, next item is 5
11
"""


# -------------
# Allocated space
# ------------
def search_for_player(self, file: list, player_name: str):
    for player in file:
        if player['name'] == player_name:
            total = player['goals'] + player['assists']
            print(f"{player['name']:21}{player['team']:3}{player['goals']:4} + {player['assists']:2} = {total:3}")
            # player['name']:21: The name will be padded to take up 21 characters in the output.


# -----------
# Pygame
# -----------
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # The colour is passed as a tuple containing the RGB values for the colour.
    window.fill((0, 255, 255))

    # After the window is filled with colour the image is drawn at the given location with the blit method.
    window.blit(robot, (x, y))

    # the contents of the window are updated with the function
    pygame.display.flip()

    # makes the image move defined pixel to the right with each iteration:
    x += velocity
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    # The method tick takes care of the speed of the animation.
    # The argument 60 dictates that the loop should be executed 60 times a second, which means that the image moves 60 pixels to the right each second.
    # This approximately matches the FPS or frames per second value used with games.
    clock.tick(60)
