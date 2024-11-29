import random

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "aquamarine", "PaleGreen", "cyan", "magenta", "lime", "gold", "gray"]

# First challenge: "Make a square"
# tim.color("red")
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)

# Second chalenge: Draw a dashed line
# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Third Challenge: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
def draw_shape(sides):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)

def change_pen_color():
    color = random.choice(colors)
    tim.pencolor(color)
    colors.remove(color)

for number_of_sides in range(3,11):
    change_pen_color()
    draw_shape(number_of_sides)



screen = Screen()
screen.exitonclick()