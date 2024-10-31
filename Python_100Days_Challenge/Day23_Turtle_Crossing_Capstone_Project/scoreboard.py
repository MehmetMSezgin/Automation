from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.show_current_level()

    def show_current_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over: {self.level}", align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.show_current_level()

