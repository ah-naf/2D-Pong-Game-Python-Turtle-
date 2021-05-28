from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from instrcut import Instruct
import time

#Create A Screen to show the Game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

#Game instruction
instruction = Instruct()


def start():
    instruction.reset_screen()
    # Create Paddle
    left_paddle = Paddle(-385, -20)
    right_paddle = Paddle(380, -20)


    # Create a Ball
    ball = Ball()

    # Show the Score
    score = Scoreboard()

    # Move the Paddle
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    screen.update()
    game_is_on = True
    while game_is_on:
        time.sleep(0.09)
        ball.move()
        screen.update()
        # Detect Collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect Collistion with Paddle
        if left_paddle.check(ball) or right_paddle.check(ball):
            ball.bounce_x()

        if ball.xcor() > 370:
            ball.reset_position()
            score.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()

        if score.check_winner(left_paddle.name, right_paddle.name):
            game_is_on = False
            ball.reset()
            left_paddle.reset_all()
            right_paddle.reset_all()
            #score.reset()

def stop():
    screen.bye()


screen.onkey(start, "space")
screen.onkey(stop, "p")


screen.update()



screen.exitonclick()