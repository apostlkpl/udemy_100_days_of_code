from turtle import Turtle, Screen
import random

screen = Screen()
# Set up the screen width, currently 500x400:
screen.setup(500, 400)
bet = screen.textinput("Make a bet!", "Which color turtle is going to win the race??\nYour choices are: red, yellow, green, cyan, blue, and magenta.")
# Creating turtles
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()
turtles = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]

# The left edge of the window is roughly at:
x_axis = -230
y_axis = -100
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

# Move all turtles to the left edge:
index = 0
for turtley in turtles:
    turtley.shape("turtle")
    turtley.color(colors[index])
    turtley.penup()
    turtley.goto(x_axis, y_axis)
    turtley.speed(5)
    y_axis += 40
    index += 1

# Make them race!
race = True
if bet:
    while race:
        for turtley in turtles:
            if turtley.xcor() > 230:
                winner = turtley.color()[0]
                if winner == bet:
                    print(f"You won!\nThe {winner} turtle finished first.\n")
                    race = False
                else:
                    print(f"You lost!\nYou chose the {bet} turtle, but the {winner} one won the race.\n")
                    race = False

            turtley.forward(random.randint(1, 10))
# Keep the screen open until the user closes the window
screen.mainloop()
