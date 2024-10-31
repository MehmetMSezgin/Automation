from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        # let generate a random chance to create a car so it will reduce frequency
        chance = random.randint(1,6)

        if chance == 1:
            car = Turtle()
            y_cordinate = random.randint(-230, 230)
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, y_cordinate)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT





