import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Default screen resolution
RESOL = (600, 600)

screen = Screen()
screen.setup(RESOL[0], RESOL[1])
# We want to manualy update the screen in gameplay
# for smoother transitions
screen.tracer(0)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
