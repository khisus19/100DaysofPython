import random

from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

player_lives = 0

keep_playing = "y"

while keep_playing == "y":

	difficulty = input("Choose a difficulty. Type 'e' for easy mode or 'h' for hard mode: ")

	# Asssign the lives according to difficulty
	if difficulty == "h":
		player_lives = 5
	else:
		player_lives = 10
	print(f"You have {player_lives} attempts remaining to guess the number.")

	# Computer chooses a random number
	comp_number = random.randint(1, 100)
	print(comp_number)

	# Player guess a number
	player_guess = int(input("Choose a number: "))

	while player_guess != comp_number and player_lives > 0:
		if player_guess > comp_number:
			print("Too high")
			player_lives -= 1
		else:
			print("Too low")
			player_lives -= 1
		
		if player_lives == 0:
			break

		print("Guess again")
		print(f"You have {player_lives} attempts remaining to guess the number.")
		player_guess = int(input("Choose a number: "))

	if player_guess == comp_number:
		print("You have guessed the number")
	else:
		print("You've run out of guesses.")
		print(f"The correct number was: {comp_number}")
	keep_playing = input("Do you want to keep playing. Type 'y' if so: ")