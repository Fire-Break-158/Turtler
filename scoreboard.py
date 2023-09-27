from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-450, 450)
        
    def updatescore(self):
        self.clear()
        self.write(f'level: {self.level}', align = 'left', font = FONT)

    def level_up(self):
        self.level += 1
        self.updatescore()

    def gameover(self):
        self.goto(0,0)
        self.write('Game Over', align = 'center', font = FONT)