from turtle import Turtle

BOARD_COLOR = "white"
SCRN_TOP_LOC = (0, 260)
FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(BOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(SCRN_TOP_LOC[0], SCRN_TOP_LOC[1])
        self.score_p1 = 0
        self.score_p2 = 0

    def say_score(self):
        self.clear()
        self.write("Player 1:   " + str(self.score_p1) + "\t\t SCORE \t\t  " + "Player 2:   " + str(self.score_p2), move = False, align = "center", font = FONT)

    def update_score(self, player):
        if player.lower() == "p1":
            self.score_p1 += 1
        elif player.lower() == "p2":
            self.score_p2 += 1
