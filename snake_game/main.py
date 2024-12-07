import random

import turtle as t
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Vibora")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.3)
    
    snake.move()

    #TODO: Detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.refresh()

    #TODO: Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        is_game_over = True

print("Game Over")

screen.exitonclick()