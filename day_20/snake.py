from turtle import Turtle, Screen

class Snake:
    def __init__(self, shape, color):
       self.snakey = []
       self.shape = shape
       self.color = color
       self.create_snake()
       self.head = self.snakey[0]

    def create_snake(self):
        xaxis = 0
        for i in range(3):
            tu = Turtle(shape = self.shape)
            tu.color(self.color)
            tu.penup()
            # position each turtle to the left of the previous one
            tu.goto(xaxis, 0)
            self.snakey.append(tu)
            # each turtle has a width of 20px
            xaxis -= tu.get_shapepoly()[0][0] - tu.get_shapepoly()[-1][0]
 
    def extend_snake(self):
        tail = Turtle(shape = self.shape)
        tail.color(self.color)
        tail.penup()
        tail.goto(self.snakey[-1].position())
        self.snakey.append(tail)

    def move_snake(self):
        # make sure the whole snake moves consistently:
        for i in range(len(self.snakey) - 1, 0, -1):
            x = self.snakey[i - 1].xcor()
            y = self.snakey[i - 1].ycor()
            self.snakey[i].goto(x, y)
        self.head.forward(20)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
