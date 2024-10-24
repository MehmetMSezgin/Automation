from turtle import Turtle

BALL_WIDTH = 20
BALL_HEIGHT = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_velocity = 0.1

    def move_the_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_velocity *= 0.95

    def bounce_x(self):
        self.x_move *= -1
        self.ball_velocity *= 0.95

    def reset_ball_position(self):
        self.goto(0,0)
        self.ball_velocity = 0.1

    def ball_change_direction(self):
        self.x_move *= -1
        self.y_move *= -1


