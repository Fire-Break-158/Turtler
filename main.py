import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.bgcolor("white")
screen.setup(width=1000, height=1000)
screen.title("Main test")
screen.tracer(0)

player = Player(screen)
carmgr = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    chancelist = [1, 2, 3, 4]
    carspawnchance = random.choice(chancelist)

    if carspawnchance == 1:
        carmgr.summoncarright()
        carmgr.summoncarleft()

    carmgr.mover()
    carmgr.movel()

    for car in carmgr.carlistr:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    for car in carmgr.carlistl:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

    if player.crossedroad():
        player.return_to_start()
        carmgr.level_up()
        scoreboard.level_up()

screen.exitonclick()