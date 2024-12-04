import random

import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Enter a color")

#TODO: Maybe use a for loop to give the turtles their shape
colors_list = ["purple", "blue", "green", "yellow", "orange", "red"]

positions = [(-220, -75), (-220, -45), (-220, -15), (-220, 15), (-220, 45), (-220, 75)]

turtle_list = []

for index, color in enumerate(colors_list):
    current_turtle = t.Turtle("turtle")
    current_turtle.penup()
    current_turtle.fillcolor(color)
    current_turtle.speed(2)
    current_turtle.setposition(positions[index])
    turtle_list.append(current_turtle)

is_game_over = False

while not is_game_over:
    for turtle in turtle_list:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() >= 210:
            print(turtle.xcor())
            print(turtle.fillcolor())
            is_game_over = True

screen.exitonclick()