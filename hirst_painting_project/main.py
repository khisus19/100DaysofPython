import random

import colorgram
import turtle as t


tim = t.Turtle()
tim.speed(0)

colors = colorgram.extract("./hirst_painting_project/hirst_1.webp", 20)

color_0 = tuple(colors[0].rgb)
color_1 = tuple(colors[4].rgb)
color_2 = tuple(colors[5].rgb)
color_3 = tuple(colors[6].rgb)
color_4 = tuple(colors[7].rgb)
color_5 = tuple(colors[8].rgb)
color_6 = tuple(colors[9].rgb)
color_7 = tuple(colors[10].rgb)
color_8 = tuple(colors[11].rgb)
color_9 = tuple(colors[12].rgb)
color_10 = tuple(colors[13].rgb)

list_of_colors = [color_0, color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9, color_10]

t.colormode(255)

def draw_spot():
    tim.color(random.choice(list_of_colors))
    tim.begin_fill()
    tim.dot(16)
    tim.end_fill()

def jump_right():
    tim.up()
    tim.forward(45)
    tim.down()

def jump_up_and_back():
    tim.up()
    tim.left(90)
    tim.forward(45)
    tim.left(90)
    for _ in range(10):
        tim.forward(45)
    tim.right(180)
    tim.down()

def complete_line():
    for _ in range(10):
        draw_spot()
        jump_right()

for _ in range(3):
    complete_line()
    jump_up_and_back()



screen = t.Screen()
screen.exitonclick()