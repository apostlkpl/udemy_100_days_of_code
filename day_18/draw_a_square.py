from turtle import Turtle, Screen

squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("blue")
screen = Screen()

for _ in range(4):
    squirtle.forward(100)
    squirtle.left(90)

screen.exitonclick()
