import turtle as t
import time

from paddle import Paddle
from ball import Ball

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()


screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.xcor() >= 330 and ball.distance(r_paddle) <= 50 or ball.xcor() <= -330 and ball.distance(l_paddle) <= 50:
        ball.bounce_in_paddle()

    # Detect the ball going out
    if ball.xcor() > 380:
        ball.reset_position()
    elif ball.xcor() < -380:
        ball.reset_position()
    
screen.exitonclick()