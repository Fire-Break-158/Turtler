import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Main test")

player = Player(STARTING_POSITION, screen)

carloops = []

for i in range(100):
    car = CarManager(screen)
    carloops.append(car)

for car in carloops:
    car.summoncar()

while game_is_on:
    time.sleep(1)
    screen.update()

screen.exitonclick()