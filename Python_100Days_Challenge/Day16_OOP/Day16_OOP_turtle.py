from turtle import Turtle, Screen


timmy = Turtle()  # do not forget to add paranthesis
print(timmy)

timmy.shape("turtle")
timmy.color("DarkOliveGreen", "chartreuse")
timmy.shapesize(5,5,3)
timmy.forward(200)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
