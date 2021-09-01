def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# test_board=('#','X','O','X','O','X','O','X','O','X')
# display_board(test_board)  
# "THESE ARE JUST TEST CASES FOR ABOVE FUNCTION"

def player_input():
    marker=' '
    while not(marker=='X'or marker=='O'):
        marker=input("Player 1, Do you want 'X' or 'O'? ").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')

# player1,player2=player_input()
# print(player1)
# print(player2)
# "THESE ARE JUST TEST CASES FOR ABOVE FUNCTION"

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return(
        (board[7]==board[8]==board[9]==mark)or
        (board[4]==board[5]==board[6]==mark)or
        (board[1]==board[2]==board[3]==mark)or
        (board[7]==board[4]==board[1]==mark)or
        (board[8]==board[5]==board[2]==mark)or
        (board[9]==board[6]==board[3]==mark)or
        (board[7]==board[5]==board[3]==mark)or
        (board[9]==board[5]==board[1]==mark)
    )

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board,position):
    return board[position] == " "

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in[1,2,3,4,5,6,7,8,9] and not(space_check(board,position)):
        position=int(input("Choose your next position (1-9): "))
    return position

def replay():
    return input("Do you want to play again 'yes' or 'no' ").lower().startswith('y')


print("WELCOME TO TIC-TAC-TOE")
while True:
    theboard=[' ']*10
    player1marker,player2marker=player_input()
    print(player1marker,player2marker)
    turn=choose_first()
    print(turn+" will go first")

    play_game=input("Are you ready to play? yes or no ").lower()

    if play_game=='yes':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='player 1':
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard,player1marker,position)

            if win_check(theboard,player1marker):
                display_board(theboard)
                print("Player 1 has Won!")
                game_on=False
            else:
                if full_board(theboard):
                    display_board(theboard)
                    print("Game is a draw")
                    break
                else:
                    turn='player 2'

        
        else:
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard,player2marker,position)

            if win_check(theboard,player2marker):
                display_board(theboard)
                print("Player 2 has Won!")
                game_on=False
            else:
                if full_board(theboard):
                    display_board(theboard)
                    print("Game is a draw")
                    break
                else:
                    turn='player 1'
    
    if not replay():
        break

