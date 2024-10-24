from turtle import Turtle

STARTING_POSITION_X = 0
STARTING_POSITION_Y = -280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION_X, STARTING_POSITION_Y)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(STARTING_POSITION_X, new_y)
