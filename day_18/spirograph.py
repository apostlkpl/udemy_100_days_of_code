from turtle import Turtle, Screen
import random

squirtle = Turtle()
squirtle.hideturtle()
radius = 200
screen = Screen()
screen.colormode(255)
squirtle.pensize(4)
squirtle.speed("fastest")

def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

direction = 0
while direction < 360:
    squirtle.setheading(direction)
    squirtle.pencolor(rand_color())
    squirtle.circle(radius)
    direction += 5

screen.exitonclick()
