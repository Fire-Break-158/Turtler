from turtle import Turtle, Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("Player test")

#class Player:
    
player = Turtle()
player.shape("turtle")
player.color("white")
player.hideturtle
player.penup()
player.setheading(90)
player.setpos(0,-450)
player.showturtle





screen.exitonclick()