from turtle import Turtle, Screen
import random

SPAWN_Y = [-400, -300, -200, -100, 0, 100, 200, 300, 400]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 50
SPAWN_X = [475, -475]
MOVE_INCREMENT = 10

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=1000, height=1000)
#screen.title("Car test")

class CarManager(Turtle):
    def __init__(self, screen, name):    
        super().__init__()
        print('hello')
        self = Turtle()
        self.hideturtle()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=3, stretch_len=1.5)
        self.penup()
        self.setheading(90)
        self.goto(random.choice(SPAWN_X), random.choice(SPAWN_Y))
        self.showturtle()

        def move(self):
            if self.xcor() == -475:
                while self.xcor != 475:
                    newx = self.xcor() + MOVE_INCREMENT
                    self.goto(newx, self.ycor())
            elif self.xcor() == 475:
                while self.xcor != -475:
                    newx = self.xcor() - MOVE_INCREMENT
                    self.goto(newx, self.ycor())

        move(self)

        pass

#screen.exitonclick()
