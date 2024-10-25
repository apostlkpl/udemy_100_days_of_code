from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong: The Game")
screen.tracer(0)

# Initialize the two paddles
r_paddle = Paddle("right")
l_paddle = Paddle("left")

# Initialize the ball
ball = Ball()

# Initialize the scoreboard
board = Scoreboard()

# Make the paddles mode
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# Start the game
game_on = True
while game_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.speed)
    board.say_score()
    # Bounce when colliding with wall:
    if ball.ycor() > 295 or ball.ycor() < - 295:
        ball.bounce("wall")
    
    # Bounce when colliding with paddles:
    if (ball.xcor() > 325 and ball.distance(r_paddle) < 50) or (ball.xcor() < -325 and ball.distance(l_paddle) < 50):
        ball.bounce("paddle")

    # Respawn ball when someone scores
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce("paddle")
        board.update_score("p1")
        board.say_score()

    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce("paddle")
        board.update_score("p2")
        board.say_score()

screen.mainloop()
