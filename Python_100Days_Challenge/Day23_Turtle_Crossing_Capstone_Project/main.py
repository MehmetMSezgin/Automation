import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Cross")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()
    #scoreboard.show_current_level()

    #detect collision
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect when player has reached the other side
    if player.ycor() > 280:
        # start position
        player.starting_position()

        # update scoreboard
        scoreboard.level_up()

        # increase car speed
        car_manager.increase_car_speed()

screen.exitonclick()
