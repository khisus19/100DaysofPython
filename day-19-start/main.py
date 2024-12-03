import turtle as t



screen = t.Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Enter a color")

purple_turtle = t.Turtle()
purple_turtle.shape("turtle")
purple_turtle.setposition(-220, 75)
purple_turtle.fillcolor("purple")


blue_turtle = t.Turtle()
blue_turtle.shape("turtle")
blue_turtle.setposition(-220, 45)
blue_turtle.fillcolor("blue")

green_turtle = t.Turtle()
green_turtle.shape("turtle")
green_turtle.setposition(-220,15)
green_turtle.fillcolor("green")

yellow_turtle = t.Turtle()
yellow_turtle.shape("turtle")
yellow_turtle.setposition(-220, -15)
yellow_turtle.fillcolor("yellow")

orange_turtle = t.Turtle()
orange_turtle.shape("turtle")
orange_turtle.setposition(-220, -45)
orange_turtle.fillcolor("orange")

red_turtle = t.Turtle()
red_turtle.shape("turtle")
red_turtle.setposition(-220, -75)
red_turtle.fillcolor("red")

#TODO: Change the order on which the turtles set in the starting position
#TODO: Make the animation slower
#TODO: Maybe use a for loop to give the turtles their shape


screen.exitonclick()