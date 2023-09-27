from turtle import Turtle, Screen
import random

SPAWN_Y1 = [-200, 0, 200, 400]
SPAWN_Y2 = [-300, -100, 100, 300]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
SPAWN_X = [475, -475]
SPEED_INCREASE = 10

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=1000, height=1000)
#screen.title("Car test")

class CarManager(Turtle):
    def __init__(self):
        self.carlistr = []     
        self.carlistl = []
        self.carspeed = STARTING_MOVE_DISTANCE  

    def summoncarleft(self):
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1.5, stretch_len=3)
        car.penup()
        car.goto(-475, random.choice(SPAWN_Y1))
        car.showturtle()
        self.carlistr.append(car)

    def level_up(self):
        self.carspeed += SPEED_INCREASE        

    def mover(self):
        for car in self.carlistl:
            car.backward(STARTING_MOVE_DISTANCE)

    def summoncarright(self):
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1.5, stretch_len=3)
        car.penup()
        car.goto(475, random.choice(SPAWN_Y2))
        car.showturtle()
        self.carlistl.append(car)

    def movel(self):
        for car in self.carlistr:
            car.forward(STARTING_MOVE_DISTANCE)



#screen.exitonclick()
