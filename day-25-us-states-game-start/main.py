import turtle as t
import pandas as pd

from state import State

screen = t.Screen()
screen.title("USA States Games")
image = "./blank_states_img.gif"

screen.addshape(image)
t.shape(image)

# Position the Turtle graphics window to the left side of the screen
screen.setup(width=800, height=600, startx=0, starty=0)

# Read the data
data = pd.read_csv("./50_states.csv")
states_list = data.state.to_list()

guessed_list = []
score = 0

while len(guessed_list) < 50:

    player_input = screen.textinput(f"{score}/50 States Correct", "Write a state name").title()

    if player_input == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_list:
                missing_states.append(state)
        print(missing_states)
        missing_states_df = pd.DataFrame(missing_states, columns=["state"])
        missing_states_df.to_csv("states_to_learn.csv")
        break

    if player_input in states_list and player_input not in guessed_list:
        player_input_row = data[data.state == player_input]
        player_input_x_coor = int(player_input_row["x"].iloc[0])
        player_input_y_coor = int(player_input_row["y"].iloc[0])
        guessed_list.append(player_input)

        score += 1
        state = State(player_input, player_input_x_coor, player_input_y_coor)
    

# states_to_learn.csv

t.mainloop()