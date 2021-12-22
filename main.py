import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
# Creating our paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Creating a ball Object
ball = Ball()
# Creating a scoreboard
scoreboard = Scoreboard()
# Controlling our paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "z")
screen.onkey(l_paddle.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detecting collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with r_paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detecting collision with l_paddle:
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting if the ball goes out of bounds
    # right_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # left_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
