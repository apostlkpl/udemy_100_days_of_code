from turtle import Turtle

COLOR ="white"
FONT = ("Arial", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_board()

    def get_score(self):
        return self.score

    def create_board(self):
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.write("Current score: " + str(self.score), move = False, align = "center", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", move = False, align = "center", font = FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write("Current score: " + str(self.score), move = False, align = "center", font = FONT)
