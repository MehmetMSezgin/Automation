from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        #self.paddle = Turtle() No need for that already Turtle inherited
        super().__init__()

        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)


