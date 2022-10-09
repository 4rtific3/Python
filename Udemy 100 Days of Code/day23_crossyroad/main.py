from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.spawn_car()
    cars.move_cars()
    
    # Detect turtle at finish line
    if player.is_at_finish():
        player.reset_pos()
        cars.level_up()
        scoreboard.level_up()
    
    # Detect turtle-car collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    
screen.exitonclick()