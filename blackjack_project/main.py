import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

def draw_a_card():
    '''It draws a ramdon card from the deck'''
    return random.choice(cards)

def calculate_score(cards: list):
    '''It calculates the sum of a list.
    If the player draw an As it counts as 11 or as 1'''
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
    

def show_current_status(p1: list, comp: list):
    '''It shows the current status of the game. Receives 2 list as arguments'''
    if calculate_score(p1) > 21 or calculate_score(comp) >= 17:
        print(f"    Your final hand: {p1}, final score: {calculate_score(p1)}")
        print(f"    Computer's final hand: {comp}, final score: {calculate_score(comp)}")
        if calculate_score(p1) > 21:
            print("You went over. You lose 😭")
        elif calculate_score(comp) > 21:
            print("Opponent went over. You win 😁")
        elif calculate_score(p1) == calculate_score(comp):
            print("Draw 🙃")
        elif calculate_score(p1) > calculate_score(comp):
            print("You win 😃")
        else:
            print("You lose 😤")

    else:
        print(f"    Your cards: {p1}, current score: {calculate_score(p1)}")
        print(f"    Computer's first card: {comp[0]}")


keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


while keep_playing != "n":

    print(logo)
    
    # Draw cards for the player
    for i in range(2):
        player_cards.append(draw_a_card())

    # Draw one card for the dealer
    dealer_cards.append(draw_a_card())
    
    show_current_status(player_cards, dealer_cards)
    
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
    while get_another_card != "n":
        player_cards.append(draw_a_card())
        show_current_status(player_cards, dealer_cards)

        if calculate_score(player_cards) > 21:
            break
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # Draw cards for the dealer
    if calculate_score(player_cards) <= 21:
        while calculate_score(dealer_cards) < 17:
            dealer_cards.append(draw_a_card())

        # Print final status
        show_current_status(player_cards, dealer_cards)

    # Ask to continue
    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player_cards = []
    dealer_cards = []