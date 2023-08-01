from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # do not update until it says so

turtle_square_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

"""Create Snake"""
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""Move Snake"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

screen.exitonclick()
