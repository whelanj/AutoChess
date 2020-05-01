import numpy as np
from math import inf as infinity
import random

game_state = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
overall_game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
players = ['X', 'O']
next_board = 1


def play_move(state, player, block_num, board_num):
    print('playing move')
    x_offset = 0
    if board_num == 2 or board_num == 5 or board_num == 8:
        x_offset = 3
    elif board_num == 3 or board_num == 6 or board_num == 9:
        x_offset = 6
    y_offset = ((board_num - 1) // 3) * 3
    x_value = (block_num - 1) % 3 + x_offset
    y_value = int((block_num - 1) / 3 + y_offset)
    if state[y_value][x_value] is ' ':
        state[int((block_num - 1) / 3 + y_offset)][(block_num - 1) % 3 + x_offset] = player
        print("returning " + str(block_num))
        return block_num
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        return play_move(state, player, block_num, board_num)


def assign_mini_winner(state, player, block_num):
    print('assigning winner')
    x_value = (block_num - 1) % 3
    y_value = int((block_num - 1) / 3)
    print(str(x_value) + str(y_value))
    if state[y_value][x_value] is ' ':
        state[y_value][x_value] = player


def check_current_state(game_state):
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"

    # Check horizontals
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Done"

    # Check verticals
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Done"

    # Check diagonals
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Done"

    return None, "Not Done"


def check_mini_state(game_state):
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Space Draw"

    # Check horizontals
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Space Won"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Space Won"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Space Won"

    # Check verticals
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Space Won"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Space Won"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Space Won"

    # Check diagonals
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Space Won"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Space Won"

    return None, "Not Done"


def print_board(game_state):
    # First row of boards
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |   | '
          + str(game_state[0][3]) + ' || ' + str(game_state[0][4]) + ' || ' + str(game_state[0][5]) + ' |   | '
          + str(game_state[0][6]) + ' || ' + str(game_state[0][7]) + ' || ' + str(game_state[0][8]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |   | '
          + str(game_state[1][3]) + ' || ' + str(game_state[1][4]) + ' || ' + str(game_state[1][5]) + ' |   | '
          + str(game_state[1][6]) + ' || ' + str(game_state[1][7]) + ' || ' + str(game_state[1][8]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |   | '
          + str(game_state[2][3]) + ' || ' + str(game_state[2][4]) + ' || ' + str(game_state[2][5]) + ' |   | '
          + str(game_state[2][6]) + ' || ' + str(game_state[2][7]) + ' || ' + str(game_state[2][8]) + ' |')
    print('----------------  ----------------  ----------------')
    # Second row of boards
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[3][0]) + ' || ' + str(game_state[3][1]) + ' || ' + str(game_state[3][2]) + ' |   | '
          + str(game_state[3][3]) + ' || ' + str(game_state[3][4]) + ' || ' + str(game_state[3][5]) + ' |   | '
          + str(game_state[3][6]) + ' || ' + str(game_state[3][7]) + ' || ' + str(game_state[3][8]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[4][0]) + ' || ' + str(game_state[4][1]) + ' || ' + str(game_state[4][2]) + ' |   | '
          + str(game_state[4][3]) + ' || ' + str(game_state[4][4]) + ' || ' + str(game_state[4][5]) + ' |   | '
          + str(game_state[4][6]) + ' || ' + str(game_state[4][7]) + ' || ' + str(game_state[4][8]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[5][0]) + ' || ' + str(game_state[5][1]) + ' || ' + str(game_state[5][2]) + ' |   | '
          + str(game_state[5][3]) + ' || ' + str(game_state[5][4]) + ' || ' + str(game_state[5][5]) + ' |   | '
          + str(game_state[5][6]) + ' || ' + str(game_state[5][7]) + ' || ' + str(game_state[5][8]) + ' |')
    print('----------------  ----------------  ----------------')
    # Third row of boards and overall board
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[6][0]) + ' || ' + str(game_state[6][1]) + ' || ' + str(game_state[6][2]) + ' |   | '
          + str(game_state[6][3]) + ' || ' + str(game_state[6][4]) + ' || ' + str(game_state[6][5]) + ' |   | '
          + str(game_state[6][6]) + ' || ' + str(game_state[6][7]) + ' || ' + str(game_state[6][8]) + ' |   | '
          + str(overall_game_state[0][0]) + ' || ' + str(overall_game_state[0][1]) + ' || ' + str(overall_game_state[0][2]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[7][0]) + ' || ' + str(game_state[7][1]) + ' || ' + str(game_state[7][2]) + ' |   | '
          + str(game_state[7][3]) + ' || ' + str(game_state[7][4]) + ' || ' + str(game_state[7][5]) + ' |   | '
          + str(game_state[7][6]) + ' || ' + str(game_state[7][7]) + ' || ' + str(game_state[7][8]) + ' |   | '
          + str(overall_game_state[1][0]) + ' || ' + str(overall_game_state[1][1]) + ' || ' + str(overall_game_state[1][2]) + ' |')
    print('----------------  ----------------  ----------------')
    print('| ' + str(game_state[8][0]) + ' || ' + str(game_state[8][1]) + ' || ' + str(game_state[8][2]) + ' |   | '
          + str(game_state[8][3]) + ' || ' + str(game_state[8][4]) + ' || ' + str(game_state[8][5]) + ' |   | '
          + str(game_state[8][6]) + ' || ' + str(game_state[8][7]) + ' || ' + str(game_state[8][8]) + ' |   | '
          + str(overall_game_state[2][0]) + ' || ' + str(overall_game_state[2][1]) + ' || ' + str(overall_game_state[2][2]) + ' |')
    print('----------------  ----------------  ----------------')


def getBestMove(state, player, board_num):
    # Picks a random move
    mini_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    x_offset = 0
    if board_num == 2 or board_num == 5 or board_num == 8:
        x_offset = 3
    elif board_num == 3 or board_num == 6 or board_num == 9:
        x_offset = 6
    y_offset = ((board_num - 1) // 3) * 3
    for i in range(3):
        for j in range(3):
            mini_state[i][j] = state[i + y_offset][j + x_offset]
    winner_check, done_check = check_mini_state(mini_state)
    print(done_check)
    if done_check == "Space Won" or done_check == "Space Draw":
        print("Mini already complete, choosing another")
        overall_attempts = []
        valid_board = False
        while not valid_board:          # While every position has not been tried
            print("Starting search loop")
            rand_board = 1
            while rand_board not in overall_attempts and not valid_board:  # If play has not been tried yet:
                rand_board = random.randint(1, 9)  # Pick random board
                x_value = (rand_board - 1) % 3
                y_value = int((rand_board - 1) / 3)
                print("Trying board " + str(rand_board) + " at " + str(x_value) + ", " + str(y_value))
                if overall_game_state[y_value][x_value] is ' ':
                    print("Found valid board")
                    valid_board = True
                else:
                    overall_attempts.append(rand_board)
                    print(overall_attempts)
        print("Using board " + str(rand_board))
        return getBestMove(state, player, rand_board)


    attempts = []
    while attempts.__len__() < 9:           # While every position has not been tried
        rand_move = random.randint(1, 9)    # Pick random play
        while rand_move not in attempts:    # If play has not been tried yet:
            x_value = (rand_move - 1) % 3
            y_value = int((rand_move - 1) / 3)
            print(str(x_value) + str(y_value))
            if mini_state[y_value][x_value] is ' ':
                return rand_move, board_num
            else:
                attempts.append(rand_move)
                print(attempts)


def check_mini_completion(game_state, board):
    # Checks for winner of mini-game
    print("Checking for winner of board " + str(board))
    mini_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    x_offset = 0
    if board == 2 or board == 5 or board == 8:
        x_offset = 3
    elif board == 3 or board == 6 or board == 9:
        x_offset = 6
    y_offset = ((board - 1) // 3) * 3
    for i in range(3):
        for j in range(3):
            mini_state[i][j] = game_state[i + y_offset][j + x_offset]
    winner_mini, done = check_mini_state(mini_state)
    print(winner_mini)
    if done == "Space Won":  # If AI won
        assign_mini_winner(overall_game_state, winner_mini, board)
        return True
    elif done == "Space Draw":  # Draw condition
        assign_mini_winner(overall_game_state, 'Z', board)
        return True
    else:
        return False            # If game is incomplete





# Playing
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
    overall_game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    game_state = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    current_state = "Not Done"
    print("\nNew Game!")
    print_board(game_state)
    player_choice = input("Choose which player goes first - X (You - the petty human) or O(The mighty AI): ")
    winner = None

    if player_choice == 'X' or player_choice == 'x':
        current_player_idx = 0
    else:
        current_player_idx = 1

    next_board = 1
    can_choose_board = True
    while current_state == "Not Done":
        current_board = next_board
        if current_player_idx == 0:  # Human's turn
            print('player turn')
            if can_choose_board:
                current_board = int(input("Choose which board to play on (1 to 9, don't choose a completed board)"))
                can_choose_board = False
            block_choice = int(input("You are currently playing on board " + str(next_board) + "! Choose where to place (1 to 9): "))
            final_choice = play_move(game_state, players[current_player_idx], block_choice, next_board)
            next_board = final_choice
            print(str(next_board))
            check_mini_completion(game_state, current_board)
            check_mini_completion(game_state, next_board)

        else:  # AI's turn
            print('ai turn')
            block_choice, current_board = getBestMove(game_state, players[current_player_idx], next_board)
            play_move(game_state, players[current_player_idx], block_choice, current_board)
            print("AI plays move: " + str(block_choice) + " on board " + str(current_board))
            next_board = block_choice
            can_choose_board = False
            check_mini_completion(game_state, current_board)
            check_mini_completion(game_state, next_board)
            if check_mini_completion(game_state, next_board):
                can_choose_board = True
        print_board(game_state)

        # Checks if overall game is over
        winner, current_state = check_current_state(overall_game_state)
        if winner is not None:
            print(str(winner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1) % 2

        if current_state is "Draw":
            print("Draw!")

    play_again = input('Wanna try again?(Y/N) : ')
    if play_again == 'N':
        print('Til next time!')
