from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPAWN_POS = [500, -500]
MOVE_INCREMENT = 10


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Car test")

#class CarManager:
    
car = Turtle()
car.hideturtle()
car.shape("square")
car.color(random.choice(COLORS))
car.shapesize(stretch_wid=3, stretch_len=1.5)
car.penup()
car.setheading(90)
car.goto(random.choice(SPAWN_POS), 0)
car.showturtle()





screen.exitonclick()