from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour from the rainbow")
COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []
y = 90
race = False


for i in COLOURS:
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(i)
    new_turtle.goto(-230, y)
    y -= 30
    all_turtles.append(new_turtle)

if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            race = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet.lower():
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You lost! The {winning_colour} turtle is the winner!")
        
    

screen.exitonclick()