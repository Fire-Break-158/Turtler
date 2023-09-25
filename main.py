import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager, a
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Main test")

#player = Player(STARTING_POSITION, screen)






#while game_is_on == True:
#for i in range(100):
car = CarManager(screen)
car.summoncar(a)

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()