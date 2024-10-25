from turtle import Turtle
SHAPE = "square"
COLOR = "white"
RESHAPE = (5, 1) # x and y axis stretching
SCR_LMT = (800, 600) # Default resolution/pixels

class Paddle(Turtle):

    def __init__(self, left_or_right):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(RESHAPE[0], RESHAPE[1])
        self.penup()
        self.left_or_right = left_or_right
        self.go_to_position()

    def go_to_position(self):
        if self.left_or_right.lower() == "left":
            self.goto(-350, 0)
        elif self.left_or_right.lower() == "right":
            self.goto(350, 0)

    def go_up(self):
        if self.ycor() < (SCR_LMT[1] // 2) - 20:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -(SCR_LMT[1] // 2) + 20:
            self.goto(self.xcor(), self.ycor() - 20)
