"""
Script to play Blacjack
Made following OOP

CLASSES:
    -Player, with attributes from every player
    -Table: inherits some attributes from player
    -Game: main methods of the game
"""

from methods import *
import time


t = 1
print("Welcome to Nessy's Casino, sir\n")
time.sleep(t)

while True:
    try:
        menu_selector()
    except ValueError as ve:
        print(f"Error, {ve}\nPlease provide proper value")
    player1.input_data()
    time.sleep(t)

    while True:
        player1.bet = int(input("Please, choose your bet, sir: "))
        if player1.bet > player1.funds:
            print("Not enough funds")
        else:
            break

    print(f"{player1.name} has {player1.funds}€ and goes with {player1.bet}€")
    print("Wish him good luck, ladies and gentlemen!\n")
    time.sleep(t)

    # Shuffling cards...
    player1.deal_card()
    dealer.deal_card()
    player1.deal_card()
    dealer.deal_card()

    print("Initial hand: ")
    print(f"{player1.name}: {player1.hand[0][0]} of {random.choice(suits)} | "
          f"{player1.hand[1][0]} of {random.choice(suits)}")
    print(f"{dealer.name}: {dealer.hand[0][0]} of {random.choice(suits)} | Hidden Card\n")
    time.sleep(t)

    # Score calculating
    # player1.calculate_score() is equal to Player.calculate_score(player1)
    # Python interpreter takes both ways
    player1.calculate_score()
    player1.ace_choice()
    dealer.calculate_score()
    print(player1.__str__())

    print("Would you like to hit or stand?")
    choice2 = input("0: Hit\n1: Stand\n")
    hit_stand(choice2)

    # Check win conditions in first round
    game.victory_status(dealer.score, player1.score)
    print(player1.__str__())
    print(dealer.__str__())
    victory_result()

    time.sleep(t)
    player1.hand.clear()
    dealer.hand.clear()

    print("Thank you for visiting our casino, sir")
    print("Would you like to play again?\n")
    try:
        menu_selector()
    except ValueError as ve:
        print(f"Error, {ve}\nPlease provide proper value")
