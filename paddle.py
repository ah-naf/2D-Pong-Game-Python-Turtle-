from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.segment = []
        self.create_paddle(x_pos, y_pos)
        self.head = self.segment[0]
        self.head.setheading(90)
        if x_pos == -385: self.name = Screen().textinput("Player 1", "Name of the First Player: ")
        else: self.name = Screen().textinput("Player 2", "Name of the Second Player: ")

    def create_paddle(self, x_pos, y_pos):
        x, y = x_pos, y_pos
        for seg in range(0,4):
            self.add_segment(x, y)
            y += 20

    def add_segment(self, x_pos, y_pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        #new_segment.setheading(90)
        new_segment.goto(x = x_pos, y = y_pos)
        self.segment.append(new_segment)

    def move_up(self):
        self.head.goto(self.head.xcor(), self.head.ycor()+20)
        for seg in range(1, len(self.segment), 1):
            new_x = self.segment[seg].xcor()
            new_y = self.segment[seg].ycor()+20
            self.segment[seg].goto(new_x, new_y)

    def move_down(self):
        for seg in range(len(self.segment)-1,-1, -1):
            new_x = self.segment[seg].xcor()
            new_y = self.segment[seg].ycor()-20
            self.segment[seg].goto(new_x, new_y)

    def up(self):
        self.head.setheading(90)
        self.move_up()

    def down(self):
        self.head.setheading(270)
        self.move_down()

    def check(self, ball):
        for seg in self.segment:
            if seg.distance(ball) < 25: return True
        return False

    def reset_all(self):
        for seg in self.segment:
            seg.reset()
