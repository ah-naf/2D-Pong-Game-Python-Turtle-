from turtle import Turtle
from scoreboard import Scoreboard


class Instruct(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.show_instruct()

    def show_instruct(self):
        self.goto(0,90)
        self.write("Pong Game", align="center", font=("Courier", 50, "normal"))
        self.goto(-10,50)
        self.write("Press Space to Play", align="center", font=("Courier", 20, "normal"))
        self.goto(-10, 20)
        self.write("Press P to Exit", align="center", font=("Courier", 18, "normal"))
        self.goto(-10, -5)
        self.write("Get 5 point to Win", align="center", font=("Courier", 12, "normal"))

    def reset_screen(self):
        self.clear()


