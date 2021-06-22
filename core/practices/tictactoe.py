# Tic Tac Toe - First Python Capstone

# Method to select a player
def playerSelection(list_players):
    while True:
        list_players[0] = input("Player 1, will you play X or O? ").upper()
        if list_players[0] == "X":
            list_players[1] = "O"
            print("Player 1 plays X and Player 2 plays O\nGood luck!!")
            break
        if list_players[0] == "O":
            list_players[1] = "X"
            print("Player 1 plays O and Player 2 plays X\nGood luck!!")
            break
        else:
            print("Please Player1, type a correct choice between X or O.")
            continue

# Method to take the input from players and print the grid according to that input
def gameGrid(grid, player_move, player):
    pmove = {player_move: player}
    grid.update(pmove)
    print(' ' + grid[9] + ' | ' + grid[8] + ' | ' + grid[7])
    print('------' * 2)
    print(' ' + grid[6] + ' | ' + grid[5] + ' | ' + grid[4])
    print('------' * 2)
    print(' ' + grid[3] + ' | ' + grid[2] + ' | ' + grid[1])

def GameGame():
    for i in playerlist:
        if i % 2 != 0:
            while True:
                move_player1 = input("Player 1, choose your movement: ")
                if move_player1 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    print("Player 1, choose a correct movement")
                    continue
                else:
                    a = int(move_player1)
                    gameGrid(positions, a, players[0])
                    break
            if checkWinner(positions, players[0]):
                break
        if i % 2 == 0:
            while True:
                move_player2 = input("Player 2, choose your movement: ")
                if move_player2 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    print("Player 2, choose a correct movement")
                    continue
                else:
                    b = int(move_player2)
                    gameGrid(positions, b, players[1])
                    break
            if checkWinner(positions, players[1]):
                break

def checkWinner(d, winner):
    if d[9] == d[8] == d[7] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[9] == d[6] == d[3] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[9] == d[5] == d[1] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[3] == d[2] == d[1] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[6] == d[5] == d[4] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[8] == d[5] == d[2] == winner:
        print("Congratulations, you have won!!!!")
        return True
    if d[7] == d[4] == d[1] == winner:
        print("Congratulations, you have won!!!!")
        return True

# Program starts here:
while True:
    ready = input("Are you ready to play? ").lower()
    if ready == "no":
        print("Maybe another time... :P")
        break
    elif ready != "yes":
        print("Please, choose between yes or no :)")
        continue

    players = ["", ""]
    positions = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    playerlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    playerSelection(players)
    print("Let's start playing! :D")
    gameGrid(positions, "", "")
    GameGame()
    again = input("You have finished the game, do you wanna play again? ")
    if again == "no":
        print("Maybe another time... :P")
        break
    elif again != "yes":
        print("Please, choose between yes or no :)")
        continue
