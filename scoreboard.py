from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align = "center", font = ("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def check_winner(self, left, right):
        if self.l_score >= 5:
            self.goto(0,20)
            self.write(f"{left} won", align="center", font=("Courier", 30, "normal"))
            self.goto(0,-15)
            self.write("Click on the screen to exit", align="center", font=("Courier", 15, "normal"))
            return True
        elif self.r_score >= 5:
            self.goto(0,20)
            self.write(f"{right} Won", align="center", font=("Courier", 30, "normal"))
            self.goto(0, -15)
            self.write("Click on the screen to exit", align="center", font=("Courier", 15, "normal"))
            return True
        return False

