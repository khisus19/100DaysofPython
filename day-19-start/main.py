import turtle as t

tim = t.Turtle()

screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(2)

def turn_left():
    tim.left(2)



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")


screen.exitonclick()