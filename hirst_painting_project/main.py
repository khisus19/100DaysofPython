import random

import colorgram
import turtle as t


tim = t.Turtle()
tim.speed(0)

# rgb_colors = []
# colors = colorgram.extract("./hirst_painting_project/hirst_1.webp", 30)

# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

list_of_colors = [(249, 248, 243), (234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]

t.colormode(255)
tim.up()
tim.hideturtle()

def draw_spot():
    tim.color(random.choice(list_of_colors))
    tim.begin_fill()
    tim.dot(16)
    tim.end_fill()

def jump_right():
    tim.forward(45)

def jump_up_and_back():
    tim.left(90)
    tim.forward(45)
    tim.left(90)
    for _ in range(10):
        tim.forward(45)
    tim.right(180)

def complete_line():
    for _ in range(10):
        draw_spot()
        jump_right()

tim.setheading(180)
tim.forward(202)
tim.setheading(270)
tim.forward(202)
tim.setheading(0)

for _ in range(10):
    complete_line()
    jump_up_and_back()



screen = t.Screen()
screen.exitonclick()