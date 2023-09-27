from turtle import Turtle, Screen

STARTING_POSITION = (0, -450)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 400
MOVE_INCREMENT = 20

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=1000, height=1000)
#screen.title("Player test")

class Player(Turtle):
    def __init__(self, screen):  
        super().__init__()
        self.screen = screen
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_len=1.25, stretch_wid=1.25)
        self.penup()
        self.setheading(90)
        self.return_to_start()
        self.showturtle()

        self.screen.listen()
        self.screen.onkey(self.go_right, "Right")
        self.screen.onkey(self.go_left, "Left")
        self.screen.onkey(self.go_up, "Up")

    def go_up(self):
        print("go up")
        new_y = self.ycor() + MOVE_DISTANCE
        self.setheading(90) 
        self.goto(self.xcor(), new_y)
        
    def go_right(self):
        print("go right")
        new_x = self.xcor() + MOVE_DISTANCE
        self.setheading(0)
        self.goto(new_x, self.ycor())

    def go_left(self):
        print("go left")
        new_x = self.xcor() - MOVE_DISTANCE
        self.setheading(180)
        self.goto(new_x, self.ycor())

    def return_to_start(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def crossedroad(self):
        if self.ycor() > FINISH_LINE_Y:

            return True
        else:
            return False