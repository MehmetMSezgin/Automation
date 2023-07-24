from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_axis_positions = [-100, -60, -20, 20, 60, 100]

for turtle_no in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_no])
    new_turtle.goto(x=-230, y=y_axis_positions[turtle_no])
    turtles.append(new_turtle)

if user_bet:  # if user bet exists
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won ! winning color is {winning_color} ")
            else:
                print(f"You lost , winning color is {winning_color}")
    if is_race_on:
        for turtle in turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)





screen.exitonclick()
