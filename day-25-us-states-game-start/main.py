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
correct_answers_list = []
score = 0

while is_game_on:

    player_input = screen.textinput(f"{score}/50 States Correct", "Write a state name").title()
    print(player_input)

    if player_input in states_list and player_input not in correct_answers_list:
        player_input_row = data[data.state == player_input]
        player_input_x_coor = int(player_input_row["x"].iloc[0])
        player_input_y_coor = int(player_input_row["y"].iloc[0])
        correct_answers_list.append(player_input)

        score += 1
        state = State(player_input, player_input_x_coor, player_input_y_coor)
    

t.mainloop()