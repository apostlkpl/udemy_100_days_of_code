from turtle import Turtle
# Ball attributes:
COLOR = "white"
SHAPE = "circle"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.speed = 0.1

    def move_ball(self):
        self.goto(self.xcor() + self.x_step, self.ycor() + self.y_step)

    def bounce(self, axis):
        # axis <str>: "wall" or "paddle"
        if axis.lower() == "wall":
            self.y_step *= -1
            self.speed *= 0.9
        elif axis.lower() == "paddle":
            self.x_step *= -1
            self.speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed = 0.1
