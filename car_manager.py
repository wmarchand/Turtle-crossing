import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.shape("square")
        # self.color(random.choice(COLORS))
        # self.shapesize(stretch_wid=1, stretch_len=2)
        # self.penup()
        # self.goto(280,random.randint(-250,280))

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        # new_x = self.xcor() - STARTING_MOVE_DISTANCE
        # self.goto(new_x,self.ycor())
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT