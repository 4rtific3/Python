from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
MOVE_DIST = 5
MOVE_INCREMENT = 10

class Cars:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DIST
    
    
    def spawn_car(self):
        spawn_chance = random.randint(1,6)
        if spawn_chance == 1:
            new_car = Turtle("square")
            new_car.pu()
            new_car.seth(180)
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLOURS))
            ycor = random.randint(-250, 250)
            new_car.goto(320, ycor)
            self.all_cars.append(new_car)
    
    
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT