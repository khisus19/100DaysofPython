import random

import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color")

# Finish line drawing
finish_line_pen = t.Turtle()
finish_line_pen.hideturtle()
finish_line_pen.penup()
finish_line_pen.setposition(225, 100)
finish_line_pen.pendown()
finish_line_pen.setposition(225, -100)

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

winner_turtle = ""

while not is_game_over:
    for turtle in turtle_list:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() >= 210:
            winner_turtle = turtle.fillcolor()
            is_game_over = True

print("You won") if user_bet == winner_turtle else print("You lost")
print(f"The winner turtle was the {winner_turtle} one")

screen.exitonclick()