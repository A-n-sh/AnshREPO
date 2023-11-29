# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import p1_random as p1

rng = p1.P1Random()

user_input = 1
game_number = 1
player_hand = 0

while user_input != 4:
    # draw random card
    print(f"Start game")

while user_input == 'y':
    # draw random card
    card_name = rng.next_int(13) + 1

    # transforming the card into value
    card_value = 0
    if card_name == 13:
        print("Your card is a King")
        card_value = 10
    elif card_name == 12:
        print("Your card is a Queen")
        card_value = 10
    elif card_name == 11:
        print("Your card is a Jack")
        card_value = 10
    elif card_name == 1:
        print("Your card is an Ace")
        card_value = 10
    elif card_name >= 2 and card_name <= 10:
        print(f"Your card is a {card_name}")
        card_value = card_name

    each_game: True

    while each_game:
        print("1. Get another card \n 2. Hold hand \n 3. Print Statistics \n 4. Exit")

    user_input = int(input("Choose an option: "))

    if user_input == 1:
        # draw another card
        card_name = rng.next_int(13) + 1

        # transforming the card into value
        card_value = 0
        if card_name == 13:
            print("Your card is a King")
            card_value = 10
        elif card_name == 12:
            print("Your card is a Queen")
            card_value = 10
        elif card_name == 11:
            print("Your card is a Jack")
            card_value = 10
        elif card_name == 1:
            print("Your card is an Ace")
            card_value = 10
        elif card_name >= 2 and card_name <= 10:
            print(f"Your card is a {card_name}")
            card_value = card_name
        # add it to the total
        player_hand += card_value
        print("Player hand is ", player_hand)
        # make sure it's not over 21
        if player_hand > 21:
            print("Dealer has won!")
            current_game = False
        # if it's 21 stop and player wins
        if player_hand == 21:
            print("Player has won! Blackjack")
            current_game = False

    if user_input == 4:
        each_game = False


# accumulate hands
# looping for games
# looping for a game
# option 1: check 21 and exceed 21
