import another_module
# print(another_module.another_variable)

# from turtle import *

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.color("chartreuse")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Ditto"])
table.add_column("Type", ["Electric", "Water", "Fire", ""])
table.align = "l"

print(table)