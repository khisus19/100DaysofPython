import turtle as t

screen = t.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Vibora")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments_list = []

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments_list.append(new_segment)



screen.exitonclick()