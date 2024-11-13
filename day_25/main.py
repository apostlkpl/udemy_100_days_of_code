from turtle import Turtle, Screen
import pandas as pd

IMAGE = "blank_states_img.gif"
TOP = (-100, 300)

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
Turtle().shape(IMAGE)

df = pd.read_csv("50_states.csv")
correct = []
score = Turtle()
score.penup()
score.hideturtle()
score.goto(TOP[0], TOP[1])
game = True
while game:
    inp = screen.textinput("Guess a State", "Guess a State name: ")
    try:
        if inp.title() in df["state"].tolist():
            name = Turtle()
            name.penup()
            name.hideturtle()
            name.goto(int(df.x[df.state == inp.title()]), int(df.y[df.state == inp.title()]))
            name.write(inp.title(), font = ("Arial", 10, "bold"))
            score.clear()
            score.write(f"Score: {len(correct) + 1} out of 50 States", font = ("Ar    ial", 18, "bold"))
            correct.append(inp.title())
        if len(correct) == len(df.state):
            game = False
    except AttributeError:
        game = False
        
score.clear()
score.write(f"Score: {len(correct)} out of 50 States", font = ("Arial", 18, "bold"))

screen.mainloop()
