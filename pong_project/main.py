import turtle as t

from paddle import Paddle 

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()