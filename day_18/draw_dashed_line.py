from turtle import Turtle, Screen

squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("blue")

for _ in range(15):
    squirtle.pencolor("black")
    squirtle.forward(10)
    squirtle.penup()
    squirtle.forward(10)
    squirtle.pendown()

screen = Screen()
screen.exitonclick()
