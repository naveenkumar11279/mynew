from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 marker X or O ?').upper()
        player1 = marker

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if (board[1] == mark and board[2] == mark and board[3] == mark) or (
            board[4] == mark and board[5] == mark and board[6] == mark) or (
            board[7] == mark and board[8] == mark and board[9] == mark) or (
            board[1] == mark and board[5] == mark and board[9] == mark) or (
            board[7] == mark and board[5] == mark and board[3] == mark) or (
            board[7] == mark and board[4] == mark and board[1] == mark) or (
            board[8] == mark and board[5] == mark and board[2] == mark) or (
            board[9] == mark and board[6] == mark and board[3] == mark):
        return True
    else:
        return False


def choose_first():
    res = random.randint(0, 1)
    if res == 0:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    if board[position]==' ':
        return True
    return False


def full_board_check(board):
    for place in board[1:]:
        if place==' ':
            return False
    return True


def player_choice(board):
    players_next_position = ' '
    while players_next_position not in range(1, 10) or not space_check(board, players_next_position):
        players_next_position = int(input("Enter the next position(1-9): "))

    return players_next_position


def replay():
    choise = ' '
    print(choise)
    while choise not in ['Y', 'N']:
        choise = input("keep playing Y/N ?").upper()
    if choise == "Y":
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
game_on = True
start_game = True

# while True:
while start_game:
    new_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(new_board)
    turn = choose_first()
    print(turn + ' will go first ')
    player1, player2 = player_input()
    # Set the game up here
    # pass
    # while game_on:
    while game_on:
        # Player 1 Turn.
        if turn == 'player1':
            print(turn)
            position = player_choice(new_board)
            place_marker(new_board, player1, position)
            display_board(new_board)
            if win_check(new_board, player1):
                print("Congratulations player1 won the game !")
                game_on = False
            else:
                if full_board_check(new_board):
                    print("The Game is TIE!")
                    break
                else:
                    turn = 'player2'
            # Player2's turn.
        else:
            print(turn)
            position = player_choice(new_board)
            place_marker(new_board, player2, position)
            display_board(new_board)
            if win_check(new_board, player2):
                print("Congratulations player2 won the game !")
                game_on = False
            else:
                if full_board_check(new_board):
                    print("The Game is TIE!")
                    break
                else:
                    turn = 'player1'
    if not replay():
        break

        # break