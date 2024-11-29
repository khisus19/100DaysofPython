from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

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
for i in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()






screen = Screen()
screen.exitonclick()