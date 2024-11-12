from turtle import Turtle

STR_POS = (0, -280)
DIST = 10
Y_MAX = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
