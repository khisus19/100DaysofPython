import turtle as t
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Vibora")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments_list = []

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments_list.append(new_segment)


is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.3)
    for seg_index in range(len(segments_list) - 1, 0, -1):
        new_x = segments_list[seg_index - 1].xcor()
        new_y = segments_list[seg_index - 1].ycor()
        segments_list[seg_index].goto(new_x, new_y)

    segments_list[0].forward(20)


screen.exitonclick()