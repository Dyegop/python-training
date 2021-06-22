import time
from classes import *

# VARIABLES
drink = ''' 
              :#:
              : :
              : :
            .'   '.
            :_____:  .___. .___.
            |     |  |   | |   |
            |     |  '. .' '. .'
            |     |    |     |
            |_____|    |     |
            :_____:   -'-   -'-
        \n'''
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ans = 1
t = 0

# Objects
player1 = Player("Default", 0, [])
dealer = Table([])
game = Game(0)

# METHODS:
# Menu choices
def menu_selector():
    print("************MAIN MENU**************")
    # input -> method that presents a prompt to the user (the optional arg of raw_input([arg])),
    # gets input from the user and returns the data input by the user on a string
    choice = input("0: Abandon the casino\n1: Drink some whisky\n2: Play Blackjack\n")
    if choice == "0":
        raise SystemExit
    elif choice == "1":
        print("Here it is your whiskey, sir")
        time.sleep(t)
        print(drink)
        time.sleep(t)
        menu_selector()
    elif choice == "2":
        pass
    else:
        print("You must select either 0, 1 or 2.\nPlease try again")
        menu_selector()

def hit_stand(choice2):
    if choice2 == "0":
        print("Player hits")
        player1.deal_card()
        player1.calculate_score()
        player1.ace_choice()
        if dealer.score < 17:
            dealer.deal_card()
    if choice2 == "1":
        print("Player stands")

def victory_result():
    if game.status == 1:
        player1.funds += player1.bet*2
        print(f"{player1.name} wins {player1.bet*2}€")
        print(f"{player1.name} has {player1.funds}€")
    elif game.status == -1:
        player1.funds -= player1.bet
        print(f"{player1.name} loses {player1.bet}€")
        print(f"{player1.name} has {player1.funds}€")
    else:
        print("Tie")

# Display score
def display_score():
    print(f"{player1.name}'s score: {player1.score}")
    print(f"{dealer.name}'s score: {dealer.score}")

def new_game():
    pass
