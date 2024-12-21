import turtle as t
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from walls import Walls

screen = t.Screen()
screen.bgcolor("black")
screen.setup(640, 640)
screen.title("Vibora")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
walls = Walls()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.2)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with walls
    if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 295 or snake.head.ycor() < -305:
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()

# TODO: Food appears in a location diferent of the snake body
# TODO: Press a key to increase snake speed
# TODO: Press a key to start a new game