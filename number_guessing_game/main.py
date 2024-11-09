from art import logo

# print(logo)

player_lives = 0

difficulty = input("Choose a difficulty. Type 'e' fro easy mode or 'h' for hard mode: ")

if difficulty == "h":
	player_lives = 5
else:
	player_lives = 10

