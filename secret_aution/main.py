from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(logo)

print("Welcome to the secret auction program.")
bidders = {}
higher_bidder = ""
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
previous_bidder = name

bidders[name] = bid

more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

while more_bidders != "no":
    print("\n" * 50)
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

for people in bidders:

    if bidders[previous_bidder] < bidders[people]:
        higher_bidder = people
        previous_bidder = people

print(f"The winner is {higher_bidder} with a bid of ${bidders[higher_bidder]}")