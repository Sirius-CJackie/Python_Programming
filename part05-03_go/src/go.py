# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    
    for item in game_board:
        for i in item:
            if i == 1 :
                player1 += 1
            elif i == 2 :
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0 