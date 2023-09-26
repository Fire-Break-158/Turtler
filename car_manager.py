from turtle import Turtle, Screen
import random

SPAWN_Y = [-300, -200, -100, 0, 100, 200, 300, 400]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 25
SPAWN_X = [475, -475]
MOVE_INCREMENT = 10

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=1000, height=1000)
#screen.title("Car test")

class CarManager(Turtle):
    def __init__(self):
        self.carlistr = []     
        self.carlistl = []  

    def summoncarleft(self):
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1.5, stretch_len=3)
        car.penup()
        car.goto(-475, random.choice(SPAWN_Y))
        car.showturtle()
        self.carlistr.append(car)

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
        car.goto(475, random.choice(SPAWN_Y))
        car.showturtle()
        self.carlistl.append(car)

    def movel(self):
        for car in self.carlistr:
            car.forward(STARTING_MOVE_DISTANCE)

#screen.exitonclick()
