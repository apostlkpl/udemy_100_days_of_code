from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()

    def spawn_food(self):
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")

    def refresh_food(self):
        x = random.randint(0, 275)
        y = random.randint(0, 275)
        self.goto(x, y)
