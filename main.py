import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

#cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()
    # if random.randint(0,10) == 0:
    #     car = CarManager()
    #     cars.append(car)
    # for i in cars:
    #     if player.distance(i) < 20:
    #         game_is_on = False
    #     i.move()

    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #next level
    # if player.ycor() > 280:
    #     scoreboard.increase_score()
    #     player.reset_position()
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()