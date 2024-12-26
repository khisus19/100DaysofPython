import turtle as t
import pandas as pd

from state import State

screen = t.Screen()
screen.title("USA States Games")
image = "./blank_states_img.gif"

screen.addshape(image)

t.shape(image)

# Read the data
data = pd.read_csv("./50_states.csv")
states_list = list(data.state)

is_game_on = True

while is_game_on:

    player_input = screen.textinput("States", "Write a state name").capitalize()

    if player_input in states_list:
        player_input_row = data[data.state == player_input]
        player_input_x_coor = int(player_input_row["x"].iloc[0])
        player_input_y_coor = int(player_input_row["y"].iloc[0])

        state = State(player_input, player_input_x_coor, player_input_y_coor)
    

t.mainloop()