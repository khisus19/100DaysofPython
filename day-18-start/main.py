import random

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.speed(0)


colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "lime", "gold", "gray", "violet", "indigo", "turquoise", "maroon", "navy", "teal", "salmon", "coral", "khaki", "orchid", "plum", "tan"]

###--------- First challenge: --------###
#           Make a square

# tim.color("red")
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)


###--------- Second chalenge: --------###
#           Draw a dashed line 

# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


###--------- Third Challenge: --------###
#            Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# def draw_shape(sides):
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

# def change_pen_color():
#     color = random.choice(colors)
#     tim.pencolor(color)
#     colors.remove(color)

# for number_of_sides in range(3,11):
#     change_pen_color()
#     draw_shape(number_of_sides)


###--------- Fourth challenge: --------###
#            Random walk

# tim.pensize(10)

# directions = (0, 90, 180, 270)

# def change_pen_color():
#     t.colormode(255)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tim.pencolor((r, g , b))

# def choose_direction():
#     tim.setheading(random.choice(directions))

# for _ in range(130):
#     choose_direction()
#     tim.forward(30)
#     change_pen_color()



###--------- Fifth challenge: --------###
#            Draw a Spirograph

def change_pen_color():
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor((r, g , b))

def draw_the_circle():
    tim.circle(100)

def change_angle():
    tim.setheading(tim.heading() + 2)

for angle in range(0, 180):
    draw_the_circle()
    change_angle()
    change_pen_color()

screen = t.Screen()
screen.exitonclick()