from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.shape("turtle")


# # Drawing a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# # Drawing a dashed line
# for i in range(10):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)


# # Drawing 2D shapes incrementally
# COLOURS = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_shape(no_sides):
#     angle = 360 / no_sides
#     timmy.color(random.choice(COLOURS))
#     for i in range(no_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for no_sides in range(3,11):
#     draw_shape(no_sides)


# # Random Walk & Tuples
# ANGLES = [0, 90, 180, 270]

def random_colour():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

# def walk(colour):
#     timmy.color(colour)
#     timmy.seth(random.choice(ANGLES))
#     timmy.forward(20)

# timmy.speed(0)
# timmy.pensize(10)
# for i in range(200):
#     colour = random_colour()
#     walk(colour)


# Drawing a spirograph

def spirograph(colour):
    timmy.color(colour)
    timmy.circle(100)

timmy.speed(0)
for angle in range(0, 361, 5):
    colour = random_colour()
    spirograph(colour)
    timmy.seth(angle)




screen = Screen()
screen.exitonclick()