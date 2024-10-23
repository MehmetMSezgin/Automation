# Break down the problem
"""
1- Create the screen
2- Create and move a paddle
3- Create another paddle
4- Create the ball and make it move
5- Detect the collision with wall and bounce
6- Detect collision with paddle
7- Detect when paddle misses
8- Keep score
"""
import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

WIDTH = 800
HEIGHT = 600

# create the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)  # stop the animation

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_the_ball()

    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
