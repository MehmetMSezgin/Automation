# keyword - Module name - keyword - thing in module
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.forward(100)
    tim.left(90)  # 90 degree

for _ in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    if _ % 2 == 0:
        tim.right(90)
        if _ % 10 == 0:
            tim.left(90)

tom = Turtle()
tom.backward(100)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)


tex = Turtle()
tex.pensize(15)
angle = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tex.speed("fastest")
for _ in range(100):
    way =random.choice(angle)
    set_colour = random.choice(colours)
    tex.color(set_colour)
    tex.forward(30)
    tex.setheading(way)

screen = Screen()
screen.exitonclick()
