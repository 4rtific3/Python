from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_COOR = [(-350, 0), (350, 0)]

screen = Screen()
ball = Ball()
player_1 = Paddle(STARTING_COOR[0])
player_2 = Paddle(STARTING_COOR[1])
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(player_1.p1_up, "w")
screen.onkey(player_1.p1_down, "s")
screen.onkey(player_2.p2_up, "Up")
screen.onkey(player_2.p2_down, "Down")



game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    # Detecting ball-wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
        
    if (ball.xcor() < -330 and ball.distance(player_1) < 40) or (ball.distance(player_2) < 40 and ball.xcor() > 340):
        ball.paddle_bounce()
        
    if ball.xcor() < -380:
        scoreboard.p2_point()
        ball.reset_position()
        
    if ball.xcor() > 380:
        scoreboard.p1_point()
        ball.reset_position()

screen.exitonclick()