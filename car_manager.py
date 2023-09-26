from turtle import Turtle, Screen
import random

SPAWN_Y = [100, 200, 300, 400, 500, 600, 700, 800, 900]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 50
SPAWN_X = [500, -500]
MOVE_INCREMENT = 10



screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Car test")

class CarManager(Turtle):
    def __init__(self, screen):    
        super().__init__()
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=3, stretch_len=1.5)
        car.penup()
        car.setheading(90)
        car.goto(random.choice(SPAWN_X), random.choice(SPAWN_Y))
        car.showturtle()

        def move(car):
            if car.xcor() == -500:
                while car.xcor != 500:
                    newx = car.xcor() + MOVE_INCREMENT
                    car.goto(newx, car.ycor())
            elif car.xcor() == 500:
                while car.xcor != -500:
                    newx = car.xcor() - MOVE_INCREMENT
                    car.goto(newx, car.ycor())

        move(car)

screen.exitonclick()