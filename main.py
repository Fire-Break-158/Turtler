import time
from turtle import Screen
#from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Main test")

#player = Player(STARTING_POSITION, screen)

car = CarManager(screen, '1')

car1 = CarManager(screen, '2')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
