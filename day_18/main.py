from turtle import Screen, Turtle
from colors import colors_list
import random

screen = Screen()
squirtle = Turtle()
screen.setworldcoordinates(-15, -10, screen.window_width() + 30 , screen.window_height() + 30)
screen.colormode(255)
squirtle.speed("fastest")
#squirtle.shape("turtle")
#squirtle.forward(100)
squirtle.hideturtle()

for j in range(15):
    if j == 0 or j % 2 == 0:
        squirtle.penup()
        squirtle.setheading(90)
        squirtle.forward(20)
        squirtle.setheading(0)
        squirtle.forward(50)
        squirtle.pendown()
    else:
        squirtle.penup()
        squirtle.setheading(90)
        squirtle.forward(100)
        squirtle.setheading(180)
        squirtle.forward(50)
        squirtle.pendown()
    for i in range(18):
        current_color = colors_list[random.randint(0, len(colors_list) - 1)]
        squirtle.pencolor(current_color)
        squirtle.fillcolor(current_color)
        squirtle.begin_fill()
        squirtle.circle(20)
        squirtle.end_fill()
        squirtle.penup()
        squirtle.forward(50)
        squirtle.pendown()

screen.exitonclick()
