import turtle as t
import time

from snake import Snake

screen = t.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Vibora")
screen.tracer(0)

snake = Snake()

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.3)
    
    snake.move()


screen.exitonclick()