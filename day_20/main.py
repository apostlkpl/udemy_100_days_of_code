from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake: The Game")
screen.tracer(0)

snake = Snake("square", "white")

food = Food()
food.spawn_food()
# Control the snake with the Arrow keys
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

# Create the score board
board = Score()
board.create_board()

speed = 0.2
game_on = True
while game_on:
    screen.update()
    # Gradually increase speed
    if board.get_score() < 5:
        time.sleep(speed)
    else:
        new_speed = speed - 0.01 * (board.get_score() // 5)
        time.sleep(new_speed)
    snake.move_snake()
        
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh_food()
        board.update_score()
        snake.extend_snake()

    # Detect collision with wall:
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        board.game_over()

    # Detect collision with own body
    for bodypart in snake.snakey[1:]:
        # excluded the snakey head
        if snake.head.distance(bodypart) < 10:
            game_on = False
            board.game_over()

screen.mainloop()
