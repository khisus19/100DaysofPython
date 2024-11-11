import random

from art import logo, vs
from game_data import data

option_a = ""
option_b = ""
higher_option = ""
current_score = 0
is_game_over = False

# Choose two random options

def fetch_random_famous(previous_person):
    '''Go fetch a random famous. If is the same than the previous gets another'''
    new_person = random.choice(data)
    while new_person == previous_person:
        new_person = random.choice(data)
    return new_person

def check_for_higher(p1, p2):
    if p1['follower_count'] > p2['follower_count']:
        return p1
    else:
        return p2
        

# Assign to the variables
option_a = fetch_random_famous(option_a)
option_b = fetch_random_famous(option_a)

print(option_a)
print(option_b)

while not is_game_over:

    # Check which is higher and assign it to the variable
    higher_option = check_for_higher(option_a, option_b)

    # Print the options
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    # Ask the player to choose
    player_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if player_input == "a":
        player_choice = option_a
    else:
        player_choice = option_b

    # Check if is correct
    correct_choice = check_for_higher(player_choice, higher_option)

    if player_choice == correct_choice:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        option_a = option_b
        option_b = fetch_random_famous(option_a)
        print(option_a)
        print(option_b)
    else:
        print(f"Sorry that's wrong. Your final score is: {current_score}")
        is_game_over = True



    # If is correct keep that option and assign to A


    # Get another random opt and assign to B. Check if is not the same