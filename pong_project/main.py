import turtle as t

from paddle import Paddle 

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle(350)

screen.listen()
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()